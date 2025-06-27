import requests
from core.colors import COL
from utils.common import save_config
from core.setup import clear_terminal  # Import your clear_terminal function
import os

def webhook_info():
    os.makedirs("Cfg", exist_ok=True)
    print(f"{COL.LIGHTCYAN_EX}\n ─── Webhook Info ──────────────────────────\n")

    url = input(f"{COL.WHITE} [•] Enter webhook URL: ").strip()
    save_config({"webhook": url})

    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            print(f"\n{COL.LIGHTGREEN_EX} Webhook Info:")
            print(f"  ID: {data.get('id')}")
            print(f"  Name: {data.get('name')}")
            print(f"  Avatar: {data.get('avatar')}")
            print(f"  Channel ID: {data.get('channel_id')}")
            print(f"  Guild ID: {data.get('guild_id')}")
            print(f"  Application ID: {data.get('application_id')}")
        else:
            print(f"{COL.LIGHTRED_EX} Failed to fetch webhook info. Status code: {response.status_code}")
    except Exception as e:
        print(f"{COL.LIGHTRED_EX} Error: {e}")

    input("\n Press Enter to return...")
    clear_terminal()
