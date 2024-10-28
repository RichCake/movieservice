from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def get_url(request):
    if request.method == "POST":
        post_data = json.loads(request.body)

    return redirect("homepage:home")
