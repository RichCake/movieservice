from django.shortcuts import render
# for test git actons

def homepage_view(request):
    return render(request, "homepage/main.html", {})
