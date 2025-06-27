import requests
from core.colors import COL
from utils.common import save_config
import os

def rename_webhook():
    os.makedirs("Cfg", exist_ok=True)
    print(f"{COL.LIGHTCYAN_EX}\n ─── Webhook Renamer ──────────────────────\n")

    url = input(f"{COL.WHITE} [•] Webhook URL: ").strip()
    new_name = input(f"{COL.WHITE} [•] New webhook name: ").strip()

    save_config({"webhook": url, "new_name": new_name})

    payload = {
        "name": new_name
    }
    headers = {
        "Content-Type": "application/json"
    }

    try:
        response = requests.patch(url, json=payload, headers=headers)
        if response.status_code == 200:
            print(f"{COL.GREEN} [✔] Webhook renamed successfully!")
        else:
            print(f"{COL.RED} [✘] Failed to rename webhook. Status code: {response.status_code}")
    except Exception as e:
        print(f"{COL.RED} [!] Error renaming webhook: {e}")

    input("\n Press Enter to return...")
