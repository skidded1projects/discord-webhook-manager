import requests
from core.colors import COL
from utils.common import save_config
import os

def check_status():
    os.makedirs("Cfg", exist_ok=True)
    print(f"{COL.LIGHTCYAN_EX}\n ─── Webhook Status Checker ────────────────\n")

    url = input(f"{COL.WHITE} [•] Enter webhook URL: ").strip()
    save_config({"webhook": url})

    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"{COL.GREEN} Webhook is valid and active!")
        elif response.status_code == 404:
            print(f"{COL.RED} Webhook is invalid or deleted.")
        else:
            print(f"{COL.RED} Status check returned status code: {response.status_code}")
    except Exception as e:
        print(f"{COL.RED} [!] Error checking webhook status: {e}")

    input("\n Press Enter to return...")
