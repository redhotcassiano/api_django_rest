from rest_framework import serializers
from .models import Music, Categories


class MusicSerializer(serializers.ModelSerializer):

    class Meta:

        model = Music
        fields = '__all__'

class CategoriesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Categories
        fields = '__all__'