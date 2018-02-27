from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('api/profiles/', include('users.api.urls', namespace="api-profiles")),
    path('posts/', include('posts.urls')),
    path('api/posts/', include('posts.api.urls', namespace="api-posts")),
    path('', TemplateView.as_view(template_name="base_layout.html"), name="homepage"),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
