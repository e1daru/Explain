#!/usr/bin/env python3
"""Install one local skill in Claude Code, Codex, or both without overwriting."""

import argparse
import os
from pathlib import Path
import shutil
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"


def file_map(folder):
    return {
        str(item.relative_to(folder)): item.read_bytes()
        for item in folder.rglob("*")
        if item.is_file()
    }


def preflight(source, destination):
    if destination.exists() or destination.is_symlink():
        if destination.is_dir() and file_map(source) == file_map(destination):
            return False
        raise FileExistsError(
            f"Existing installation differs: {destination}. "
            "Move it out of the skills directory before installing this version."
        )
    return True


def install_skill(source, destination):
    if not preflight(source, destination):
        return "Already installed"
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(source, destination)
    if file_map(source) != file_map(destination):
        raise RuntimeError(f"Installed files did not verify: {destination}")
    return "Installed"


def main():
    names = sorted(folder.name for folder in SKILLS.iterdir() if (folder / "SKILL.md").is_file())
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--host", choices=["claude", "codex", "both"], default="both")
    parser.add_argument("--skill", choices=names, default="explain")
    args = parser.parse_args()
    source = SKILLS / args.skill
    claude_root = Path(os.environ.get("CLAUDE_CONFIG_DIR") or (Path.home() / ".claude")).expanduser()
    roots = {"claude": claude_root / "skills", "codex": Path.home() / ".agents" / "skills"}
    hosts = ["claude", "codex"] if args.host == "both" else [args.host]
    targets = [(host, roots[host] / args.skill) for host in hosts]
    try:
        for host, destination in targets:
            preflight(source, destination)
        for host, destination in targets:
            print(f"{install_skill(source, destination)} for {host}: {destination}")
    except (OSError, RuntimeError) as error:
        parser.exit(1, f"{error}\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
