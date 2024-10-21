from django.contrib import admin

from distributions.models import Distribution


@admin.register(Distribution)
class DistributionAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "first_send_date",
        "first_send_time",
        "period",
        "status",
        "owner",
        "letter",
    )
    list_filter = ("owner",)
    ordering = ("first_send_date",)
