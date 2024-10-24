from django.contrib import admin

from distributions.models import Distribution, Attempt


@admin.register(Distribution)
class DistributionAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "first_send_date",
        "first_send_time",
        "last_send_date",
        "last_send_time",
        "period",
        "status",
        "owner",
        "letter",
    )
    list_filter = ("owner",)
    ordering = ("first_send_date",)


@admin.register(Attempt)
class AttemptAdmin(admin.ModelAdmin):
    list_display = ('id', 'last_attempt', 'status', 'server_answer', 'distributions', 'owner')
    list_filter = ('status',)
    search_fields = ('last_attempt', 'server_answer',)
