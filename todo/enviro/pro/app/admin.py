from django.contrib import admin

from .models import Task
class MemberAdmin(admin.ModelAdmin):
    list_display = "taskname", "starttime", "endtime", "description"
admin.site.register(Task,MemberAdmin )