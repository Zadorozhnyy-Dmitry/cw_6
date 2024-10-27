from django import forms

from clients.models import Client
from distributions.forms import StyleFormMixin


class ClientsForm(StyleFormMixin, forms.ModelForm):
    """
    Класс для описания формы клиента
    """

    class Meta:
        model = Client
        fields = (
            "name",
            "client_email",
            "comments",
        )
