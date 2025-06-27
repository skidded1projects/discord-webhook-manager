import requests
from core.colors import COL
from utils.common import save_config
import os

def send_message():
    os.makedirs("Cfg", exist_ok=True)
    print(f"{COL.LIGHTCYAN_EX}\n ─── Webhook Messenger ────────────────────\n")

    url = input(f"{COL.WHITE} [•] Webhook URL: ").strip()
    message = input(f"{COL.WHITE} [•] Message to send: ").strip()

    save_config({"webhook": url, "last_message": message})

    try:
        response = requests.post(url, json={"content": message})
        if response.status_code in [200, 204]:
            print(f"{COL.GREEN} [✔] Message sent!")
        else:
            print(f"{COL.RED} [✘] Failed to send message. Status code: {response.status_code}")
    except Exception as e:
        print(f"{COL.RED} [!] Error sending message: {e}")

    input("\n Press Enter to return...")
