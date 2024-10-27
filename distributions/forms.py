from django import forms

from distributions.models import Distribution


class DistributionForm(forms.ModelForm):
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
