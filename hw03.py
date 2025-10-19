import sys
from pathlib import Path
from colorama import Fore, Style, init

init(autoreset=True)
COLOR_DIR = Fore.BLUE + Style.BRIGHT
COLOR_FILE = Fore.GREEN


def display_dir_structure(path: Path, prefix: str = ""):
    if not path.is_dir():
        return
    
    try:
        items = sorted(list(path.iterdir()))
    except Exception as e:
        print(f"Помилка доступу до директорії {path}: {e}")
        return

    for index, item in enumerate(items):
        is_last = index == len(items) - 1
        pointer = "└── " if is_last else "├── "
        new_prefix = prefix + ("    " if is_last else "│   ")
        print(prefix + pointer, end="")
        
        if item.is_dir():
            print(f"{COLOR_DIR}📦 {item.name}")
            display_dir_structure(item, new_prefix)
        elif item.is_file():
            print(f"{COLOR_FILE}📜 {item.name}")


def main():
    if len(sys.argv) < 2:
        print(f"{Fore.RED}Помилка: Необхідно передати шлях до директорії як аргумент.")
        print(f"{Fore.YELLOW}Використання: python {Path(sys.argv[0]).name} /шлях/до/директорії")
        return
    
    target_path_str = sys.argv[1]
    target_path = Path(target_path_str)

    if not target_path.exists():
        print(f"{Fore.RED}Помилка: Шлях '{target_path_str}' не існує.")
        return
    
    if not target_path.is_dir():
        print(f"{Fore.RED}Помилка: Шлях '{target_path_str}' не є директорією.")
        return

    print(f"{Style.BRIGHT}Структура директорії: {target_path_str}{Style.RESET_ALL}")
    print(f"{COLOR_DIR}📦 {target_path.name}")
    display_dir_structure(target_path, "│   ")


if __name__ == "__main__":
    main()