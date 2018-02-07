# __author__ = {{cookiecutter.full_name}}
import rest_framework_filters as filter
from api.models import {{cookiecutter.default_model}}


class {{cookiecutter.default_model}}Filter(filter.FilterSet):
    class Meta:
        model = {{cookiecutter.default_model}}
        fields = tuple()
