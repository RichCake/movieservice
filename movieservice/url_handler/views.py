from django.shortcuts import redirect

def get_url(request):
    playerUrl = request.GET.get('playerUrl')
    movie = request.GET.get('movie')
    movie_id = request.GET.get('id')
    # Печатаем параметры для отладки
    print(f"Player URL: {playerUrl}, Movie: {movie}, ID: {movie_id}")
    return redirect("homepage:home")
