# __author__ = {{cookiecutter.full_name}}
from rest_framework.permissions import BasePermission


class {{cookiecutter.default_model}}Permission(BasePermission):
    """Demo permission"""

    def has_permission(self, request, view):
        return True
