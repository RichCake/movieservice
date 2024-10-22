from django.shortcuts import render

def player_view(request):
    return render(request, "player/index.html", {})
