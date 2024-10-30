from django.shortcuts import render
# for test git actonsjh

def homepage_view(request):
    return render(request, "homepage/main.html", {})
