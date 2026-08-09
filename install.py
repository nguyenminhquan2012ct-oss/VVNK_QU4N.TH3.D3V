import subprocess
import sys

PACKAGES = [
    "discord.py-self",
    "aiohttp",
    "requests",
    "pynacl",
    "pytz",
    "psutil",
    "colour",
    "python-dateutil",
    "instaloader",
]

def install_package(package):
    try:
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", package],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        print(f"  [+] {package} - thanh cong")
        return True
    except subprocess.CalledProcessError:
        print(f"  [-] {package} - that bai")
        return False

def main():
    print("=" * 50)
    print("  VVNK - Cai dat thu vien")
    print("=" * 50)
    print()

    success = 0
    fail = 0

    for pkg in PACKAGES:
        result = install_package(pkg)
        if result:
            success += 1
        else:
            fail += 1

    print()
    print(f"  Hoan thanh: {success} thanh cong, {fail} that bai")
    print()

    if fail > 0:
        input("Nhan Enter de thoat...")

if __name__ == "__main__":
    main()
