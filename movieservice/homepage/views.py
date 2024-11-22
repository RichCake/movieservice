import json

from django.shortcuts import render, redirect
from django.conf import settings

from movie_history.models import History


def homepage_view(request):
    if not request.user.is_authenticated:
        return redirect("homepage:about")
    movies = History.objects.filter(user=request.user).order_by("-id")
    for movie in movies:
        if not isinstance(movie.movie_data, dict):
            movie.movie_data = json.loads(movie.movie_data)
    fake_kinopoisk_api_keq = settings.FAKE_KINOPOISK_API_KEY
    return render(
        request,
        "homepage/main.html",
        {"movies": movies, "FAKE_KINOPOISK_API_KEY": fake_kinopoisk_api_keq})


def about_view(request):
    return render(request, "homepage/about.html", {})
