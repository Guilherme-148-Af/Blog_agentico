from news_framework import BaseNewsAgent
import asyncio
import httpx


class AgenteDemo(BaseNewsAgent):

    def __init__(self):
        super().__init__(
    agent_name="Agente Demo",
    topic="Demo"
)
        self.agent_name = "Agente Demo"

        # ⚠️ METE AQUI O IP DO PROFESSOR
        self.hub_url = "http://192.168.51.42:8080/publish"

        self.token = "epf2026_secret"

    async def collect_data(self):
        await asyncio.sleep(1)

        return {
            "title": "Primeiro Agente Operacional",
            "content": "Este é um teste do sistema agêntico para o 2.º ano.",
            "url": "http://192.168.0.132:8080"
        }

    async def process_with_ai(self, data):
        await asyncio.sleep(0.5)

        data["summary"] = "O sistema está configurado e pronto para receber os agentes dos alunos!"
        return data

    # 🔥 ESTE É O MAIS IMPORTANTE
    async def run(self):
        data = await self.collect_data()
        processed = await self.process_with_ai(data)

        payload = {
            "agent_name": self.agent_name,
            "topic": self.topic,
            "title": processed["title"],
            "summary": processed["summary"],
            "url": processed["url"],
            "confidence": 0.99
        }

        headers = {
            "x-token": self.token
        }

        async with httpx.AsyncClient() as client:
            response = await client.post(
                self.hub_url,
                json=payload,
                headers=headers
            )

            print("Status:", response.status_code)
            print("Resposta:", response.text)