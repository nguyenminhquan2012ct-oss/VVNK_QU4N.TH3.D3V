import sys, time, os, subprocess

LOG_FILE = "bot.log"

def find_python():
    for p in ["python", "python3", "py"]:
        try:
            subprocess.run([p, "--version"], capture_output=True, timeout=3)
            return p
        except:
            pass
    return "python"

def is_bot_running():
    try:
        result = subprocess.run(
            ["tasklist", "/FI", "WINDOWTITLE eq VVNK*", "/FI", "IMAGENAME eq python.exe"],
            capture_output=True, text=True, timeout=5
        )
        if "python.exe" in result.stdout:
            return True
        result2 = subprocess.run(
            ["wmic", "process", "where", "commandline like '%bot.py%'", "get", "processid"],
            capture_output=True, text=True, timeout=5
        )
        lines = [l.strip() for l in result2.stdout.splitlines() if l.strip() and l.strip() != "ProcessId"]
        if lines:
            return True
    except:
        pass
    return False

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"\033[1;36m{'='*50}\033[0m")
    print(f"\033[1;36m         VVNK - LOG VIEWER\033[0m")
    print(f"\033[1;36m{'='*50}\033[0m")
    print(f"\033[1;33mWatching: {os.path.abspath(LOG_FILE)}\033[0m")
    print(f"\033[1;36m{'-'*50}\033[0m")

    if not os.path.exists(LOG_FILE):
        open(LOG_FILE, 'w', encoding='utf-8').close()

    pos = 0
    check_count = 0
    while True:
        try:
            size = os.path.getsize(LOG_FILE)
            if size < pos:
                pos = 0
            if size > pos:
                with open(LOG_FILE, 'r', encoding='utf-8', errors='replace') as f:
                    f.seek(pos)
                    new = f.read()
                    if new:
                        sys.stdout.write(new)
                        sys.stdout.flush()
                pos = size

            check_count += 1
            if check_count >= 50:
                check_count = 0
                if not is_bot_running():
                    time.sleep(1)
                    if not is_bot_running():
                        print(f"\n\033[1;31m[LOG] Bot da dung. Log viewer dong theo.\033[0m")
                        time.sleep(2)
                        break

            time.sleep(0.1)
        except KeyboardInterrupt:
            break
        except Exception:
            time.sleep(0.5)

if __name__ == "__main__":
    main()
