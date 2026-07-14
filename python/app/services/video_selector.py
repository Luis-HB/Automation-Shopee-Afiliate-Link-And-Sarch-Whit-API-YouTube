class VideoSelector:

    @staticmethod
    def escolher(videos):

        if not videos:
            return None

        videos.sort(

            key=lambda v: v.score,

            reverse=True

        )

        return videos[0]