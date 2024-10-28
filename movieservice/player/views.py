from django.shortcuts import render
import json


def player_view(request):
    movie_data = json.dumps({"kinopoisk": "4626783", "title": "«Пчеловод» (The Beekeeper, 2024)"})

    return render(request, "player/index.html", {"data": movie_data})
