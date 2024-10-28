from django.shortcuts import render

def player_view(request):
    return render(request, "player/index.html", {"data": '"{\"kinopoisk\":\"4626783\",\"title\":\"«Пчеловод» (The Beekeeper, 2024)\"}"'})
