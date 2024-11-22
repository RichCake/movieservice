import json

from django.shortcuts import render, redirect

from movie_history.models import History


def homepage_view(request):
    if not request.user.is_authenticated:
        return redirect("homepage:about")
    movies = History.objects.filter(user=request.user).order_by("-id")
    for movie in movies:
        if not isinstance(movie.movie_data, dict):
            movie.movie_data = json.loads(movie.movie_data)
    return render(request, "homepage/main.html", {"movies": movies})


def about_view(request):
    return render(request, "homepage/about.html", {})
