# __author__ = {{cookiecutter.full_name}}

from django.urls import path, include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register('{{cookiecutter.default_model.lower()}}', views.{{cookiecutter.default_model}}ViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
