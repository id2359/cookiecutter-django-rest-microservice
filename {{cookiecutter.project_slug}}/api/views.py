# __author__ = {{cookiecutter.full_name}}
from api.models import {{cookiecutter.default_model}}
from rest_framework import viewsets
from api.permissions import {{cookiecutter.default_model}}Permission

class {{cookiecutter.default_model}}ViewSet(viewsets.ModelViewSet):
    queryset = {{cookiecutter.default_model}}
    permission_classes = [{{cookiecutter.default_model}}Permission, ]
