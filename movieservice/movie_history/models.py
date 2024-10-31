from django.db import models
from django.conf import settings


class History(models.Model):
    movie_data = models.JSONField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
