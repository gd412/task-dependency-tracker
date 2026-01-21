from django.contrib import admin
from .models import Task, TaskDependency

class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'status', 'created_at', 'updated_at')
    list_filter = ('status', 'created_at')
    search_fields = ('title', 'description')

admin.site.register(Task, TaskAdmin)
admin.site.register(TaskDependency)
