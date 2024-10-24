from django.contrib import admin

from clients.models import Client


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    """
    Админка клиента
    """
    list_display = (
        "id",
        "name",
        "client_email",
        "comments",
        "owner",
    )
    list_filter = ("owner", "client_email",)
