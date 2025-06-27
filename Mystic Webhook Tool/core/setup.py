import os
import platform

def set_terminal(title="Mystic Hooks - Crab Console"):
    if platform.system() == "Windows":
        os.system("mode 90,27")
        os.system(f"title {title}")
    else:
        os.system('printf "\e[8;27;90t"')
        os.system(f'echo -ne "\033]0;{title}\007"')

def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")
