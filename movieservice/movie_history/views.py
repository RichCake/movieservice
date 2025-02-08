import json
from django.db import transaction
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import requests
import re
from .models import History, Movie


def get_or_fetch_movie(link):
    # Извлекаем часть ссылки в формате /film/{id} или /series/{id}
    match = re.search(r'/(film|series)/\d+/', link)
    if not match:
        return None  # Если часть ссылки не найдена

    db_link = match.group(0)  # Например, /film/45319/ или /series/45319/

    # Проверяем в базе данных
    movie = Movie.objects.filter(link=db_link).first()
    if movie:
        return movie.name  # Если нашли фильм в базе, возвращаем название

    # Если фильма нет в базе, подготавливаем ID для API
    # if not db_link.startswith('/film/'):
    #     # Если это серия, преобразуем в /film/{id}
    #     db_link = db_link.replace('/series/', '/film/')

    # Извлекаем ID из ссылки
    movie_id = re.search(r'\d+', db_link).group(0)

    # Делаем запрос к API
    api_url = f'https://kinopoiskapiunofficial.tech/api/v2.2/films/{movie_id}'
    headers = {
        'X-API-KEY': 'b727d67c-aee0-47bf-b59d-f83353fbea0f',
        'Content-Type': 'application/json',
    }

    response = requests.get(api_url, headers=headers)

    if response.status_code != 200:
        return None  # Ошибка при запросе к API

    data = response.json()

    # Проверяем, что есть поле nameRu
    if data and 'nameRu' in data:
        # Сохраняем фильм в базу данных
        new_movie = Movie.objects.create(
            link=f'/film/{movie_id}/',  # Сохраняем как /film/{id}/
            name=data['nameRu'],
            year=data.get('year', None)
        )
        return new_movie.name  # Возвращаем название фильма

    return None  # Если данные не удалось получить


@csrf_exempt 
def fetch_movie(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        link = data.get('link')

        if not link:
            return JsonResponse({'error': 'Link is required'}, status=400)

        # Используем функцию для получения фильма
        movie_name = get_or_fetch_movie(link)

        if movie_name:
            return JsonResponse({'name': movie_name})
        else:
            return JsonResponse({'name': link})

    return JsonResponse({'error': 'Invalid method'}, status=405)


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
        try:
            # Проверяем корректность данных
            post_data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)

        # Создаём запись в истории
        try:
            History.objects.create(movie_data=post_data, user=request.user)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return redirect("homepage:home")


def is_auth(request):
    return JsonResponse({"is_auth": request.user.is_authenticated})
