import json

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from movie_history.models import History


@login_required
def player_view(request):
    return render(request, "player/index.html", {"data": None})
