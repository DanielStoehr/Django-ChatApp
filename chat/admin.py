from django.contrib import admin
from .models import Chat, Message

# Register your models here.


class MessageAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'author', 'text', 'receiver')


admin.site.register(Message, MessageAdmin)
admin.site.register(Chat)
