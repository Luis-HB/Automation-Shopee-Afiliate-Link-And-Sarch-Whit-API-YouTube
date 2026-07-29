from dataclasses import dataclass

from models.commercial.metric import Metric


@dataclass
class VideoAnalysis:

    total_videos: Metric

    average_views: Metric

    average_likes: Metric

    average_duration: Metric

    engagement: Metric

    content_quality: Metric

    diversity: Metric

    commercial_strength: Metric