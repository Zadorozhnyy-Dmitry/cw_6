from django import forms

from distributions.forms import StyleFormMixin
from letters.models import Letter


class LettersForm(StyleFormMixin, forms.ModelForm):
    """
    Класс для описания формы письма
    """
    class Meta:
        model = Letter
        fields = ('topic', 'body',)