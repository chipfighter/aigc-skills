"""从 skills/ 生成各技能下载包；只使用 Python 标准库。"""

from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED


def main():
    root = Path(__file__).resolve().parent.parent
    downloads = root / "downloads"
    downloads.mkdir(exist_ok=True)
    for skill in sorted((root / "skills").iterdir()):
        if not (skill / "SKILL.md").is_file():
            continue
        with ZipFile(downloads / f"{skill.name}.zip", "w", ZIP_DEFLATED) as archive:
            for path in sorted(skill.rglob("*")):
                if path.is_file() and "__pycache__" not in path.parts:
                    archive.write(path, (Path(skill.name) / path.relative_to(skill)).as_posix())
            archive.write(root / "LICENSE", f"{skill.name}/LICENSE")
        print(f"{skill.name}.zip")


if __name__ == "__main__":
    main()
