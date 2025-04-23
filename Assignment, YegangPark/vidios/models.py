from datetime import timedelta
from django.db import models
import logging



logger = logging.getLogger(__name__)


class Lecturer(models.Model):
    name = models.CharField("Lecturer Name", max_length=100, unique=True)

    def __str__(self):
        return self.name





class Topic(models.Model):
    name = models.CharField("Topic", max_length=100, unique=True)

    def __str__(self):
        return self.name


class Timestamp(models.Model):
    lecture = models.ForeignKey("Lecture", on_delete=models.CASCADE, related_name="timestamps")
    time = models.DurationField("Timestamp")  # e.g. 00:12:34
    label = models.CharField("Section label", max_length=100)  # e.g. "Introduction"

    def __str__(self):
        return f"{self.label} @ {self.time}"



class Lecture(models.Model):
    video_url = models.URLField("Video URL", max_length=1000)
    lecture_title = models.CharField("Lecture title", max_length=100)
    lecturers = models.ManyToManyField(
        Lecturer,
        related_name="lectures",
        verbose_name="Lecturers",
        blank=False
    )

    lecture_date = models.DateField("Lecture date")
    location = models.CharField("Lecture location", max_length=100)
    lecture_topics = models.ManyToManyField(Topic, related_name="lectures")
    lecture_summary = models.CharField("Summary", max_length=500)
    lecture_length = models.DurationField("Video duration", blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.video_url and not self.lecture_length:
            try:
                from .utils import fetch_duration_with_api
                duration = fetch_duration_with_api(self.video_url)
                if duration:
                    self.lecture_length = duration
            except Exception as e:
                # production 에선 로깅만 하고 넘어가세요
                import logging
                logging.getLogger(__name__).error(f"YT API fetch 실패: {e}")
        super().save(*args, **kwargs)
