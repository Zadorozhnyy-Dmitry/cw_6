from django import forms

from distributions.models import Distribution


class StyleFormMixin:
    """
    Миксин для стилизации формы
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class DistributionForm(StyleFormMixin, forms.ModelForm):
    """
    Класс для описания формы рассылки
    """

    class Meta:
        model = Distribution
        fields = (
            "first_send_date",
            "first_send_time",
            "last_send_date",
            "last_send_time",
            "period",
            "clients",
            "letter",
        )
