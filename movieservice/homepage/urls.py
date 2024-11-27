from django.urls import path, include
from django.views.generic import TemplateView

from . import views

app_name = 'homepage'

urlpatterns = [
    path('', views.homepage_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('privacy/', views.policy, name='privacy'),
]
