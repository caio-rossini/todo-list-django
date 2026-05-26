from django.contrib import admin
from .models import Task, Tag

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ["content", "is_done", "created_at", "deadline"]
    list_filter = ["is_done", "tags"]

admin.site.register(Tag)
