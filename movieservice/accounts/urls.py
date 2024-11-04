from django.urls import path
from .views import SignUpView, CustomLoginView, profile, ChangePasswordView
from django.contrib.auth import views as auth_views


app_name = "accounts"

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/', profile, name='users-profile'),
    path('password_change/', ChangePasswordView.as_view(), name='password_change'),
]

# Я пока не решил нужно ли это.
# Но если указать это здесь, а не в core, то работать не будет.
# Будет переводить на logout/login админа
    # path('login/', CustomLoginView.as_view(redirect_authenticated_user=True, template_name='registration/login.html'), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),