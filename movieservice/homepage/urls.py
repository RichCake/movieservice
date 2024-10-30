from django.urls import path, include

from . import views

app_name = 'homepage'

urlpatterns = [
    path('', views.homepage_view, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
]
