from django.urls import path, include

from . import views

app_name = 'homepage'

urlpatterns = [
    path('', views.homepage_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('accounts/', include('django.contrib.auth.urls')),
]
