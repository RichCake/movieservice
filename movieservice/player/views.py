from django.http import JsonResponse
from django.shortcuts import render
from get_name_kp import get_kp_name_by_link


def player_view(request):
    return render(request, "player/index.html")


def get_title(request):
    if request.method == "GET":
        link = request.GET.get("link", None)
        if link:
            try:
                title = get_kp_name_by_link(link)
                return JsonResponse({"success": True, "title": title})
            except Exception as e:
                return JsonResponse({"success": False, "error": str(e)})
        return JsonResponse({"success": False, "error": "No link provided"})
    return JsonResponse({"success": False, "error": "Invalid request method"})
