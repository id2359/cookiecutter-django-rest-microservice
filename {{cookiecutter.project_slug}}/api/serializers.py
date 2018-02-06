# __author__ = {{cookiecutter.full_name}}
from rest_framework import serializers

from api.models import Demo


class DemoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Demo
