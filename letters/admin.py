from django.contrib import admin

from letters.models import Letter


@admin.register(Letter)
class LetterAdmin(admin.ModelAdmin):
    """
    Админка для сообщения клиенту
    """
    list_display = (
        'id',
        'topic',
        'body',
        'owner',
    )
