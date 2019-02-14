from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from myapi.api import CategoriesViewSets, MusicsViewSets

route = routers.DefaultRouter()

route.register('categories', CategoriesViewSets)
route.register('musics', MusicsViewSets)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(route.urls))
]
