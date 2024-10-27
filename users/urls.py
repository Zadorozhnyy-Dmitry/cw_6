from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from users.apps import UsersConfig
from users.views import RegisterView, ProfileView

app_name = UsersConfig.name

urlpatterns = [
    path("", LoginView.as_view(template_name="users/login.html"), name="login"),  # Вход
    path("logout/", LogoutView.as_view(), name="logout"),  # Выход
    path("register/", RegisterView.as_view(), name="register"),  # Регистрация
    path("profile/", ProfileView.as_view(), name="profile"),  # Редактирование профиля
]
