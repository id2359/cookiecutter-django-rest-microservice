# __author__ = {{cookiecutter.full_name}}
import rest_framework_filters as filter
from api.models import Demo


class DemoFilter(filter.FilterSet):
    class Meta:
        model = Demo
        fields = tuple()
