from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from users.models import User


class UserRegisterForm(UserCreationForm):
    """
    Форма для регистрации пользователя
    """

    class Meta:
        model = User
        fields = (
            "email",
            "password1",
            "password2",
        )


class UserProfileForm(UserChangeForm):
    """
    Форма для редактирования профиля пользователя
    """

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "email",
        )

    def __init__(self, *args, **kwargs):
        """
        Скрываю поле пароля из формы
        """
        super().__init__(*args, **kwargs)

        self.fields["password"].widget = forms.HiddenInput()
