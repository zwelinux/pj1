from django.contrib import admin
from .models import Task, TaskType

admin.site.site_header = 'Simple Task'                    # default: "Django Administration"
admin.site.index_title = 'Simple Task Management '                 # default: "Site administration"
admin.site.site_title = 'adminsitration'

class TaskAdmin(admin.ModelAdmin):
	list_display = ['title', 'content', 'start', 'end', 'date']
	list_filter = ['start', 'end', 'date']
	search_fields = ['title', 'content']

admin.site.register(Task, TaskAdmin)
admin.site.register(TaskType)