import json

from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from .models import History



@csrf_exempt
@login_required
def add_movie(request):
    if request.method == "POST":
        post_data = json.loads(request.body)
        History.objects.create(movie_data=post_data, user=request.user)

    return redirect("homepage:home")


def is_auth(request):
    return JsonResponse({"is_auth": request.user.is_authenticated})
