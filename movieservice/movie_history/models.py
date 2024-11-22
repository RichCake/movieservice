from django.db import models
from django.conf import settings
from django.utils import timezone
from datetime import timedelta


class History(models.Model):
    movie_data = models.JSONField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def time_since_creation(self):
        now = timezone.now()
        delta = now - self.created_at

        if delta < timedelta(minutes=1):
            return f"{delta.seconds} секунд назад"
        elif delta < timedelta(hours=1):
            return f"{delta.seconds // 60} минут назад"
        elif delta < timedelta(days=1):
            return f"{delta.seconds // 3600} часов назад"
        elif delta < timedelta(weeks=1):
            return f"{delta.days} дней назад"
        elif delta < timedelta(days=30):
            return f"{delta.days // 7} недель назад"
        elif delta < timedelta(days=365):
            return f"{delta.days // 30} месяцев назад"
        else:
            return f"{delta.days // 365} лет назад"
