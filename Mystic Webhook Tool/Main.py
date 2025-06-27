from core.banner import banner
from core.setup import set_terminal, clear_terminal
from core.colors import COL
from utils.spammer import spam_webhook
from utils.messenger import send_message
from utils.deleter import delete_webhook
from utils.renamer import rename_webhook
from utils.info import webhook_info
from utils.status import check_status
import time

def main():
    set_terminal()
    while True:
        clear_terminal()
        print(banner)
        choice = input(f'{COL.LIGHTMAGENTA_EX}   ╚═ Mystic@Crab >> ').strip()

        if choice == "1":
            spam_webhook()
        elif choice == "2":
            send_message()
        elif choice == "3":
            webhook_info()
        elif choice == "4":
            delete_webhook()
        elif choice == "5":
            rename_webhook()
        elif choice == "6":
            check_status()
        elif choice == "99":
            print(f"{COL.RED}Exiting Mystic Hooks...")
            time.sleep(1)
            break
        else:
            print(f"{COL.RED}Invalid option. Try again.")
            time.sleep(1.5)

if __name__ == "__main__":
    main()
