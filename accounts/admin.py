from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Diary)
admin.site.register(Follower)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Tag)
admin.site.register(Notification)
