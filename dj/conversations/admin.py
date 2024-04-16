from django.contrib import admin

from .models import Conversations, ConversationsMessage

admin.site.register(Conversations)
admin.site.register(ConversationsMessage)