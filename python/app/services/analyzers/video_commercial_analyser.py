from statistics import mean

from models.commercial.metric import Metric
from models.commercial.video_analysis import VideoAnalysis


class VideoCommercialAnalyzer:

    # =====================================================

    def analyze(self, context):

        videos = context.videos

        if not videos:

            return self._empty()

        return VideoAnalysis(

            total_videos=self._total_videos(videos),

            average_views=self._average_views(videos),

            average_likes=self._average_likes(videos),

            average_duration=self._average_duration(videos),

            engagement=self._engagement(videos),

            diversity=self._diversity(videos),

            content_quality=self._content_quality(videos),

            commercial_strength=self._commercial_strength(videos)

        )

    # =====================================================

    def _empty(self):

        return VideoAnalysis(

            total_videos=Metric("NONE", 0),

            average_views=Metric("NONE", 0),

            average_likes=Metric("NONE", 0),

            average_duration=Metric("NONE", 0),

            engagement=Metric("NONE", 0),

            diversity=Metric("NONE", 0),

            content_quality=Metric("NONE", 0),

            commercial_strength=Metric("NONE", 0)

        )
    
    def _total_videos(self, videos):

        total = len(videos)

        if total >= 20:
            level = "EXCELLENT"

        elif total >= 10:
            level = "HIGH"

        elif total >= 5:
            level = "GOOD"

        elif total >= 2:
            level = "LOW"

        else:
            level = "VERY_LOW"

        return Metric(level, total)
    
    def _average_views(self, videos):

        value = int(

            mean(

                video.views

                for video in videos

            )

        )

        if value >= 300000:
            level = "EXCELLENT"

        elif value >= 100000:
            level = "HIGH"

        elif value >= 30000:
            level = "GOOD"

        elif value >= 5000:
            level = "LOW"

        else:
            level = "VERY_LOW"

        return Metric(level, value)
    
    def _average_likes(self, videos):

        value = int(

            mean(

                video.likes

                for video in videos

            )

        )

        if value >= 300000:
            level = "EXCELLENT"

        elif value >= 100000:
            level = "HIGH"

        elif value >= 30000:
            level = "GOOD"

        elif value >= 5000:
            level = "LOW"

        else:
            level = "VERY_LOW"

        return Metric(level, value)
    
    def _average_duration(self, videos):

        value = int(

            mean(

                video.duracao

                for video in videos

            )

        )

        if 40 <= value <= 90:

            level = "GOOD"

        elif 20 <= value < 40:

            level = "MEDIUM"

        else:

            level = "LOW"

        return Metric(level, value)
    
    def _engagement(self, videos):

        values = []

        for video in videos:

            if video.views:

                values.append(

                    video.likes / video.views

                )

        if not values:

            return Metric("NONE", 0)

        engagement = mean(values)

        if engagement >= 0.08:

            level = "EXCELLENT"

        elif engagement >= 0.05:

            level = "HIGH"

        elif engagement >= 0.03:

            level = "GOOD"

        else:

            level = "LOW"

        return Metric(

            level,

            round(engagement, 4)

        )
        
    def _diversity(self, videos):

        channels = {

            video.canal

            for video in videos

        }

        total = len(channels)

        if total >= 10:

            level = "HIGH"

        elif total >= 5:

            level = "GOOD"

        else:

            level = "LOW"

        return Metric(level, total)
    
    
    def _content_quality(self, videos):

        value = mean(

            video.score

            for video in videos

        )

        if value >= 90:

            level = "EXCELLENT"

        elif value >= 75:

            level = "HIGH"

        elif value >= 60:

            level = "GOOD"

        else:

            level = "LOW"

        return Metric(

            level,

            round(value,2)

        )
        
    def _commercial_strength(self, videos):

        views = self._average_views(videos)

        engagement = self._engagement(videos)

        quality = self._content_quality(videos)

        score = 0

        weights = {
            "EXCELLENT": 4,
            "HIGH": 3,
            "GOOD": 2,
            "MEDIUM": 1,
            "LOW": 0,
            "VERY_LOW": 0,
            "NONE": 0,
        }

        score += weights.get(views.level, 0)
        score += weights.get(engagement.level, 0)
        score += weights.get(quality.level, 0)

        if score >= 10:
            level = "EXCELLENT"
        elif score >= 7:
            level = "HIGH"
        elif score >= 4:
            level = "GOOD"
        else:
            level = "LOW"

        return Metric(level, score)