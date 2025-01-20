from django.contrib import admin
from .models import Issue, Status

class IssueAdmin(admin.ModelAdmin):
    list_display = [
        "name", "summary", "reporter", "assignee", "created_on"
    ]

class StatusAdmin(admin.ModelAdmin):
    status_display = [
        "name"
    ]

admin.site.register(Issue, IssueAdmin)
admin.site.register(Status, StatusAdmin)

# Register your models here.
