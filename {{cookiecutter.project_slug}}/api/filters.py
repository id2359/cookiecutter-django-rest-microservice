# __author__ = {{cookiecutter.full_name}}
from api.models import Demo
import rest_framework_filters as filter


class DemoFilter(filter.FilterSet):
    class Meta:
        model = Demo
        fields = tuple()
