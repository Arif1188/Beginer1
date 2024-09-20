from django.contrib import admin
from .models import TaskMdoel, LevelModel


admin.site.register(LevelModel)

@admin.register(TaskMdoel)
class TaskModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'is_active']
    list_display_links = ['id', 'title']
    list_filter = ['is_active']
    readonly_fields = ['is_active']
    search_fields = ['title']
