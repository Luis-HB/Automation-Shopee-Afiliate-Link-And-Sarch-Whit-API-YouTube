from services.youtube_service import YouTubeService

yt = YouTubeService("AIzaSyBIO9cao_eIzwqJmpwnWtROwEgtgelaJeg")

videos = yt.buscar_shorts("Mouse Logitech G203")

for video in videos:

    print("=" * 80)
    print(video["titulo"])
    print(video["url"])
    print("Views:", video["views"])
    print("Likes:", video["likes"])
    print("Duração:", video["duracao"], "segundos")