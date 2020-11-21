from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter
from backend.demo.utils import get_all_forks, get_user_from_github
from backend.demo.api.views import ProjectListView, MemberListView

router = DefaultRouter()
router.register('project', ProjectListView)
router.register('member', MemberListView)

catchall = TemplateView.as_view(template_name='index.html')

urlpatterns = [
    path('', catchall),
    path('admin/', admin.site.urls),
    path('add-fork', get_all_forks),
    path('add-member', get_user_from_github),
    path('api/', include(router.urls))

    # path('api/project', ProjectListView.as_view())
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
