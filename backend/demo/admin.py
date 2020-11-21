from django.contrib import admin
from .models import Demo, Project, MLHMember


class ProjectEntry(admin.ModelAdmin):
    list_display = ("name", "description", "avatar_url", "project_url")

class MLHMemberEntry(admin.ModelAdmin):
    list_display = ("name", "avatar_url", "member_url")


admin.site.register(Demo)
admin.site.register(Project, ProjectEntry)
admin.site.register(MLHMember, MLHMemberEntry)