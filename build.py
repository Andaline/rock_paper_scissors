import os
import shutil
import subprocess
from zipfile import ZipFile

PROJECT_NAME = "rock_paper_scissors"
DIST_DIR = "dist"
BUILD_DIR = "build"
EXE_NAME = "main.exe"
ICON_PATH = "game/assets/icon.ico"

def clean():
    if os.path.exists(DIST_DIR):
        shutil.rmtree(DIST_DIR)
    if os.path.exists(BUILD_DIR):
        shutil.rmtree(BUILD_DIR)
    if os.path.exists(f"{PROJECT_NAME}.zip"):
        os.remove(f"{PROJECT_NAME}.zip")

def build_exe():
    subprocess.run([
        "pyinstaller",
        "--onefile",
        "--windowed",
        f"--icon={ICON_PATH}",
        "main.py"
    ], check=True)

def package_zip():
    with ZipFile(f"{PROJECT_NAME}.zip", "w") as zipf:
        for folder in [DIST_DIR, "game", "network", "profiles", "tests"]:
            for root, _, files in os.walk(folder):
                for file in files:
                    path = os.path.join(root, file)
                    zipf.write(path, arcname=os.path.relpath(path))

        # Also include these top-level files
        for file in ["main.py", "menu.py", "requirements.txt", "README.md"]:
            if os.path.exists(file):
                zipf.write(file)

def run():
    print("Cleaning old builds...")
    clean()
    print("Building executable...")
    build_exe()
    print("Packaging into zip...")
    package_zip()
    print("✅ Done! Check 'dist/' and the final zip.")

if __name__ == "__main__":
    run()