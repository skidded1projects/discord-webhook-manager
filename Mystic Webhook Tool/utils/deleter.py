import requests
from core.colors import COL
from utils.common import save_config
import os

def delete_webhook():
    os.makedirs("Cfg", exist_ok=True)
    print(f"{COL.LIGHTCYAN_EX}\n ─── Webhook Deleter ──────────────────────\n")

    url = input(f"{COL.WHITE} [•] Enter Webhook URL to delete: ").strip()
    save_config({"webhook": url})

    confirm = input(f"{COL.RED} Are you sure you want to DELETE this webhook? (y/n): ").lower()
    if confirm != 'y':
        print(f"{COL.YELLOW} Deletion cancelled.")
        input("\n Press Enter to return...")
        return

    try:
        res = requests.delete(url)
        if res.status_code == 204:
            print(f"{COL.GREEN} [✔] Webhook deleted successfully!")
        else:
            print(f"{COL.RED} [✘] Failed to delete webhook. Status code: {res.status_code}")
    except Exception as e:
        print(f"{COL.RED} [!] Error deleting webhook: {e}")

    input("\n Press Enter to return...")
