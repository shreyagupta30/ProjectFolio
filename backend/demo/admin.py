from django.contrib import admin
from .models import Demo, Project, MLHMember, Commit


class ProjectEntry(admin.ModelAdmin):
    list_display = ("name", "description", "avatar_url", "project_url", "commits_url")

class MLHMemberEntry(admin.ModelAdmin):
    list_display = ("name", "avatar_url", "member_url")

class CommitEntry(admin.ModelAdmin):
    list_display = ("author", "project", "description", "commit_url")

admin.site.register(Demo)
admin.site.register(Project, ProjectEntry)
admin.site.register(MLHMember, MLHMemberEntry)
admin.site.register(Commit, CommitEntry)
