import asyncio
import os
from twitch import TwitchMiner  # Zakładam, że TwitchMiner to główny obiekt obsługujący mining (może wymagać adaptacji)

# Lista danych logowania do kont
ACCOUNTS = [
    {"username": "user1", "password": "pass1"},
    {"username": "user2", "password": "pass2"},
    # Dodaj kolejne konta
]

async def run_on_account(account):
    cookies_path = f"cookies_{account['username']}.jar"
    miner = TwitchMiner(
        username=account["username"],
        password=account["password"],
        cookies_path=cookies_path,
        # Dodaj inne parametry wymagane przez Twój konstruktor
    )
    await miner.login()
    await miner.start_mining()

async def main():
    tasks = [run_on_account(acc) for acc in ACCOUNTS]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())