from django import forms

from letters.models import Letter


class LettersForm(forms.ModelForm):
    """
    Класс для описания формы письма
    """
    class Meta:
        model = Letter
        fields = ('topic', 'body',)