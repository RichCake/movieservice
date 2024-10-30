import json

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from movie_history.models import History


@login_required
def homepage_view(request):
    movies = History.objects.filter(user=request.user).order_by("-id")
    for movie in movies:
        movie.movie_data = json.loads(movie.movie_data)
    return render(request, "homepage/main.html", {"movies": movies})
