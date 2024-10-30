import json

from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from .models import History


def last_movie(request):
    movie_data = History.objects.filter(user=request.user).order_by("-id").first().movie_data

    return render(request, "player/index.html", {"data": movie_data})


def set_movie(request, id):
    movie_data = History.objects.filter(user=request.user).get(id=id).movie_data

    return render(request, "player/index.html", {"data": movie_data})


@csrf_exempt
@login_required
def add_movie(request):
    if request.method == "POST":
        post_data = json.loads(request.body)
        History.objects.create(movie_data=post_data, user=request.user)

    return redirect("homepage:home")


def is_auth(request):
    return JsonResponse({"is_auth": request.user.is_authenticated})
