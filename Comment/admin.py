from django.contrib import admin
from Comment.models import Comment

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name','text','created_time','email','website')

admin.site.register(Comment)
# Register your models here.
