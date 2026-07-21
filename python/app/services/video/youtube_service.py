import re
import requests
from core.config.settings import YOUTUBE_API_KEY


class YouTubeService:

    SEARCH_URL = "https://www.googleapis.com/youtube/v3/search"
    VIDEOS_URL = "https://www.googleapis.com/youtube/v3/videos"

    def __init__(self, api_key=None):

        self.api_key = api_key or YOUTUBE_API_KEY
        
        if not self.api_key:
            raise ValueError("YOUTUBE_API_KEY não configurada.")

    def buscar(self, termo, maxResults=20):

        params = {
            "key": self.api_key,
            "part": "snippet",
            "q": f"{termo} shorts",
            "type": "video",
            "maxResults": maxResults,
            "regionCode": "BR",
            "relevanceLanguage": "pt",
            "order": "relevance"
        }

        response = requests.get(
            self.SEARCH_URL,
            params=params,
            timeout=30
        )
        response.raise_for_status()

        return response.json()

    def buscar_detalhes(self, video_ids):

        params = {
            "key": self.api_key,
            "part": "snippet,statistics,contentDetails",
            "id": ",".join(video_ids)
        }

        response = requests.get(
            self.VIDEOS_URL,
            params=params,
            timeout=30
        )
        response.raise_for_status()

        return response.json()

    @staticmethod
    def iso8601_to_seconds(duration):

        horas = minutos = segundos = 0

        h = re.search(r"(\d+)H", duration)
        m = re.search(r"(\d+)M", duration)
        s = re.search(r"(\d+)S", duration)

        if h:
            horas = int(h.group(1))

        if m:
            minutos = int(m.group(1))

        if s:
            segundos = int(s.group(1))

        return horas * 3600 + minutos * 60 + segundos

    def buscar_shorts(self, termo, maxResults=20):

        busca = self.buscar(termo, maxResults)

        video_ids = [
            item["id"]["videoId"]
            for item in busca.get("items", [])
            if item.get("id", {}).get("videoId")
        ]

        if not video_ids:
            return []

        detalhes = self.buscar_detalhes(video_ids)

        videos = []

        for item in detalhes.get("items", []):

            segundos = self.iso8601_to_seconds(
                item["contentDetails"]["duration"]
            )

            # Shorts normalmente possuem até 3 minutos
            if segundos > 180:
                continue

            videos.append({
                "video_id": item["id"],
                "titulo": item["snippet"]["title"],
                "url": f"https://www.youtube.com/watch?v={item['id']}",
                "thumbnail": item["snippet"]["thumbnails"]["high"]["url"],
                "canal": item["snippet"]["channelTitle"],
                "views": int(item["statistics"].get("viewCount", 0)),
                "likes": int(item["statistics"].get("likeCount", 0)),
                "duracao": segundos
            })

        videos.sort(
            key=lambda x: (
                x["views"],
                x["likes"]
            ),
            reverse=True
        )

        return videos

    @staticmethod
    def filtrar_produto(videos, termo):
        palavras = [
            p.lower()
            for p in termo.split()
            if len(p) > 2
        ]

        resultado = []

        for video in videos:

            titulo = video["titulo"].lower()

            if all(p in titulo for p in palavras):
                resultado.append(video)

        return resultado

    # Aliases de compatibilidade para chamadas em inglês
    def search_shorts(self, query, max_results=20, **kwargs):
        return self.buscar_shorts(termo=query, maxResults=max_results)

    def search(self, query, max_results=20, **kwargs):
        return self.buscar(termo=query, maxResults=max_results)