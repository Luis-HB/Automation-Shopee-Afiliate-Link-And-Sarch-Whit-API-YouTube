class VideoSelector:

    @staticmethod
    def escolher(videos):

        if not videos:
            return None

        videos.sort(
            key=lambda v: getattr(v, "score", 0),
            reverse=True
        )

        return videos[0]