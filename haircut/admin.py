from django.contrib import admin
from .models import comment 


# Register your models here.
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'comment']

admin.site.register(Comment, CommentAdmin)

