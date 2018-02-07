# __author__ = {{cookiecutter.full_name}}
from api.models import Demo
from rest_framework import serializers


class DemoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Demo
