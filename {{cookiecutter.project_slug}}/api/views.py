# __author__ = {{cookiecutter.full_name}}
from api.models import Demo
from rest_framework import viewsets


class DemoViewSet(viewsets.ModelViewSet):
    queryset = Demo
