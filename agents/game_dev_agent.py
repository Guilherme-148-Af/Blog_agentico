import httpx
from news_framework import BaseNewsAgent
import asyncio


class GameDevNewsAgent(BaseNewsAgent):

    def __init__(self):
        super().__init__(
            "Game Dev News Agent",
            "Desenvolvimento de Novos Jogos"
        )

        self.hub_url = "https://news2pi.onrender.com/publish"
        self.token = "epf2026_secret"

    async def collect_data(self):
        return {
            "title": "Novos Jogos em Desenvolvimento: tendências e destaques atuais",
            "content": (
                "A indústria dos videojogos continua em forte evolução, com vários estúdios "
                "a apostar em novos projetos, mundos abertos, inteligência artificial, gráficos "
                "mais realistas e experiências multijogador mais imersivas. Muitos jogos recentes "
                "encontram-se em fase de desenvolvimento, revelando trailers, testes beta, acesso "
                "antecipado e atualizações constantes para a comunidade."
            ),
            "url": "https://www.gamespot.com/news/"
        }

    async def process_with_ai(self, data):
        summary = (
            "Resumo relacionado com o desenvolvimento de novos jogos, preparado para publicação no hub. "
            "A notícia destaca tendências atuais da indústria, como IA, mundos abertos, trailers, "
            "betas e acesso antecipado."
        )

        return {
            "agent_name": self.agent_name,
            "topic": self.topic,
            "title": data["title"],
            "summary": summary,
            "url": data["url"],
            "confidence": 0.95
        }

    async def run(self):
        print("AGENT A CORRER...")

        data = await self.collect_data()
        processed = await self.process_with_ai(data)

        headers = {
            "Content-Type": "application/json",
            "x-token": self.token
        }

        try:
            async with httpx.AsyncClient(timeout=20.0) as client:
                response = await client.post(
                    self.hub_url,
                    json=processed,
                    headers=headers
                )

            print("RESULTADO FINAL:")
            print(processed)
            print("STATUS:", response.status_code)
            print("RESPOSTA:", response.text)

        except Exception as e:
            print("Erro ao enviar para hub:", e)


if __name__ == "__main__":
    asyncio.run(GameDevNewsAgent().run())