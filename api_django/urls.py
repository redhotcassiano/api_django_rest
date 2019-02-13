from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from myapi.api import CategoriesViewSets

route = routers.DefaultRouter()

route.register('categories', CategoriesViewSets)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(route.urls))
]
