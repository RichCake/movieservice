from django.urls import path

from . import views

app_name = 'hist'

urlpatterns = [
    path('add/', views.add_movie, name='add'),
    path('auth/', views.is_auth, name='is_auth'),  # перенести в auth
    path('last/', views.last_movie, name='last'),
    path('<int:id>/', views.set_movie, name='set'),
]
