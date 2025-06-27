import time
import requests
import threading
import os
from core.colors import COL
from utils.common import save_config

def spam_webhook():
    os.makedirs("Cfg", exist_ok=True)
    print(f"{COL.LIGHTCYAN_EX}\n ─── Webhook Spammer ──────────────────────\n")

    url = input(f"{COL.WHITE} [•] Webhook URL: ").strip()
    message = input(f"{COL.WHITE} [•] Message to spam: ").strip()
    amount = input(f"{COL.WHITE} [•] How many times (leave blank for infinite): ").strip()
    delay_input = input(f"{COL.WHITE} [•] Delay between messages in seconds (default 1.25): ").strip()
    multi = input(f"{COL.WHITE} [•] Enable multi-threaded spam? (y/n): ").strip().lower() == "y"

    save_config({"webhook": url, "last_message": message})

    infinite = amount == ""
    if not infinite:
        try:
            amount = int(amount)
            if amount < 1:
                print(f"{COL.LIGHTYELLOW_EX} [!] Amount must be 1 or more, defaulting to 10{COL.RESET}")
                amount = 10
        except ValueError:
            print(f"{COL.LIGHTYELLOW_EX} [!] Invalid amount input, defaulting to 10{COL.RESET}")
            amount = 10

    try:
        delay = float(delay_input) if delay_input else 1.25
        if delay < 0:
            print(f"{COL.LIGHTYELLOW_EX} [!] Delay can't be negative, defaulting to 1.25s{COL.RESET}")
            delay = 1.25
    except ValueError:
        print(f"{COL.LIGHTYELLOW_EX} [!] Invalid delay input, defaulting to 1.25s{COL.RESET}")
        delay = 1.25

    count = 0
    stop_flag = threading.Event()

    def spam_loop():
        nonlocal count
        try:
            while infinite or count < amount:
                if stop_flag.is_set():
                    break
                res = requests.post(url, json={"content": message})
                if res.status_code in [200, 204]:
                    count += 1
                    print(f"{COL.GREEN} [✔] Sent message #{count}{COL.RESET}")
                elif res.status_code == 429:
                    retry_after = float(res.headers.get("retry-after", delay))
                    print(f"{COL.LIGHTYELLOW_EX} [!] Rate limited! Sleeping {retry_after}s{COL.RESET}")
                    time.sleep(retry_after)
                    continue
                else:
                    print(f"{COL.LIGHTRED_EX} [✘] Failed ({res.status_code}){COL.RESET}")
                time.sleep(delay)
        except Exception as e:
            print(f"{COL.LIGHTRED_EX} [!] Error: {e}{COL.RESET}")

    print(f"{COL.LIGHTGREEN_EX}\n Starting spam... Press Ctrl+C to stop.\n{COL.RESET}")
    try:
        if multi:
            threads = []
            for _ in range(3):
                t = threading.Thread(target=spam_loop)
                t.start()
                threads.append(t)
            for t in threads:
                t.join()
        else:
            spam_loop()
    except KeyboardInterrupt:
        stop_flag.set()
        print(f"{COL.LIGHTYELLOW_EX}\n [!] Stopped at {count} messages. Crab out! 🦀{COL.RESET}")
    input(f"\n{COL.WHITE} Press Enter to return...{COL.RESET}")
