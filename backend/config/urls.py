from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter
from backend.demo.utils import get_all_forks, get_user_from_github, get_commits
from backend.demo.api.views import ProjectListView, MemberListView, CommitListView

router = DefaultRouter()
router.register('project', ProjectListView)
router.register('member', MemberListView)
router.register('commit', CommitListView)


catchall = TemplateView.as_view(template_name='index.html')

urlpatterns = [
    path('', catchall),
    path('admin/', admin.site.urls),
    path('add-fork', get_all_forks),
    path('add-member', get_user_from_github),
    path('add-commits', get_commits),
    path('api/', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)