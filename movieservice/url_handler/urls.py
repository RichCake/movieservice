from django.urls import path

from . import views

app_name = 'url_handler'

urlpatterns = [
    path('', views.get_url, name='get'),
]
