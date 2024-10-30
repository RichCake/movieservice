from django.urls import path

from . import views

app_name = 'hist'

urlpatterns = [
    path('add/', views.add_movie, name='add'),
    path('auth/', views.is_auth, name='is_auth'),
]
