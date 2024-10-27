from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from users.apps import UsersConfig
from users.views import (
    UserCreateView,
    UserPasswordResetView,
    UserInValidEmail,
    ProfileView,
)
from users.views import email_verification

app_name = UsersConfig.name

urlpatterns = [
    path("login/", LoginView.as_view(template_name="users/login.html", extra_context={"title": "Вход"}), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),  # Выход
    path("register/", UserCreateView.as_view(), name="register"),  # Регистрация
    path("email-confirm/<str:token>/", email_verification, name="email-confirm"),  # Валидация почты при регистрации
    path("password-reset/", UserPasswordResetView.as_view(), name="password_reset"),  # Сброс пароля
    path("invalid-email/", UserInValidEmail.as_view(), name="invalid_email"),  # Если нет такого адреса
    path("profile/", ProfileView.as_view(), name="profile"),  # Профиль
]
