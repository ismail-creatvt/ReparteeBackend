from django.contrib import admin
from app.models import User, Group, Message, Membership, Conversation

admin.site.register(User)
admin.site.register(Group)
admin.site.register(Conversation)
admin.site.register(Message)
admin.site.register(Membership)

