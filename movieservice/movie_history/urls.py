from django.urls import path

from . import views

app_name = 'hist'

urlpatterns = [
    path('add/', views.add_movie, name='add'),
]
