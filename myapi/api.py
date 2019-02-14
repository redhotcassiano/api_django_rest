from rest_framework import viewsets
from myapi.serializers import CategoriesSerializer, MusicSerializer
from myapi.models import Categories, Music


class CategoriesViewSets(viewsets.ModelViewSet):
    serializer_class = CategoriesSerializer
    queryset = Categories.objects.all()

class MusicsViewSets(viewsets.ModelViewSet):
    serializer_class = MusicSerializer
    queryset = Music.objects.all()