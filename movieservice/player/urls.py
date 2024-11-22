from django.urls import path

from . import views

app_name = 'player'

urlpatterns = [
    path('', views.player_view, name='home'),
    path('get-title/', views.get_title, name='get_title')
]
