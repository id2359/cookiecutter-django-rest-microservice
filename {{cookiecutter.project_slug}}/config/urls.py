# __author__ = {{cookiecutter.full_name}}

from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('docs/', include_docs_urls('My API', authentication_classes=(), permission_classes=())),
    path('api/v1/', include('api.urls')),
    path(settings.ADMIN_URL, admin.site.urls),
]
