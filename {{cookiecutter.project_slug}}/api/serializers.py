# __author__ = {{cookiecutter.full_name}}
from api.models import {{cookiecutter.default_model}}
from rest_framework import serializers


class {{cookiecutter.default_model}}Serializer(serializers.ModelSerializer):
    class Meta:
        model = {{cookiecutter.default_model}}
        fields = "__all__"
