from rest_framework import serializers
from .models import Music, Categories
from django.contrib.auth.models import User


class UsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'


class CategoriesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Categories
        user = UsersSerializer(read_only=True)
        fields = ('name', 'description', 'user')


class MusicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Music
        category = CategoriesSerializer(many=True, read_only=True)
        user = UsersSerializer()
        fields = ('title', 'artist', 'album', 'user', 'category')
