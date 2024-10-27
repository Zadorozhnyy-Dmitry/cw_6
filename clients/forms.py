from django import forms

from clients.models import Client


class ClientsForm(forms.ModelForm):
    """
    Класс для описания формы клиента
    """
    class Meta:
        model = Client
        fields = ("name", "client_email", "comments",)
