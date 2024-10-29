import json

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from movie_history.models import History


@login_required
def player_view(request):
    movie_data = History.objects.filter(user=request.user).first().movie_data

    return render(request, "player/index.html", {"data": movie_data})
