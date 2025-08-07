import asyncio
from typing import List, Dict
from twitch import TwitchMiner  # Zakładamy, że TwitchMiner to główny obiekt miningujący

class MultiAccountManager:
    def __init__(self, accounts: List[Dict[str, str]]):
        self.accounts = accounts
        self.miners = []

    async def start_all(self):
        tasks = []
        for acc in self.accounts:
            miner = TwitchMiner(
                username=acc["username"],
                password=acc["password"],
                cookies_path=f"cookies_{acc['username']}.jar"
            )
            self.miners.append(miner)
            tasks.append(self._run_miner(miner))
        await asyncio.gather(*tasks)

    async def _run_miner(self, miner):
        await miner.login()
        await miner.start_mining()

if __name__ == "__main__":
    accounts = [
        {"username": "user1", "password": "pass1"},
        {"username": "user2", "password": "pass2"}
    ]
    manager = MultiAccountManager(accounts)
    asyncio.run(manager.start_all())