from rest_framework import viewsets
from myapi.serializers import CategoriesSerializer
from myapi.models import Categories


class CategoriesViewSets(viewsets.ModelViewSet):
    serializer_class = CategoriesSerializer
    queryset = Categories.objects.all()
