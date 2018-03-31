from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from rest_framework_jwt.views import obtain_jwt_token
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('api/users/', include('users.api.urls', namespace="api-users")),
    path('posts/', include('posts.urls')),
    path('api/posts/', include('posts.api.urls', namespace="api-posts")),
    path('api/auth/token/', obtain_jwt_token),
    # path('', TemplateView.as_view(template_name="base_layout.html"), name="homepage"),
    path('', views.homepage, name="homepage"),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
