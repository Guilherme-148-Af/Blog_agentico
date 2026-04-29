import asyncio
from agents.game_dev_agent import GameDevNewsAgent

async def main():
    agente = GameDevNewsAgent()
    await agente.run()

if __name__ == "__main__":
    asyncio.run(main())