from django.urls import path, include

from . import views

app_name = 'player'

urlpatterns = [
    path('', views.player_view, name='home'),
]
