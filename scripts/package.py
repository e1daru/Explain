#!/usr/bin/env python3
"""Build reproducible skill ZIPs from the public skills directory."""

import hashlib
from pathlib import Path
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
DIST = ROOT / "dist"


def build_zip(destination, files):
    with zipfile.ZipFile(destination, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for item in files:
            if item.is_symlink():
                raise ValueError(f"Refusing to package a symlink: {item}")
            info = zipfile.ZipInfo(str(item.relative_to(SKILLS)), date_time=(2026, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, item.read_bytes())
    with zipfile.ZipFile(destination) as archive:
        if archive.testzip() is not None:
            raise RuntimeError(f"Archive integrity check failed: {destination}")


def main():
    DIST.mkdir(exist_ok=True)
    archives = []
    all_files = []
    for folder in sorted(SKILLS.iterdir()):
        if not (folder / "SKILL.md").is_file():
            continue
        files = sorted(item for item in folder.rglob("*") if item.is_file() and item.suffix == ".md")
        destination = DIST / f"{folder.name}.zip"
        build_zip(destination, files)
        archives.append(destination)
        all_files.extend(files)
    combined = DIST / "all-skills.zip"
    build_zip(combined, all_files)
    archives.append(combined)
    checksums = "".join(f"{hashlib.sha256(item.read_bytes()).hexdigest()}  {item.name}\n" for item in sorted(archives))
    (DIST / "SHA256SUMS.txt").write_text(checksums)
    print(f"Built {len(archives)} verified archives in {DIST}")


if __name__ == "__main__":
    main()
