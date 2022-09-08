from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from library import viewsets as bookviewsets


route = routers.DefaultRouter()
route.register(r'books/', bookviewsets.BookViewSets, basename='Books')


urlpatterns = [
    path('', include(route.urls)),
    path('admin/', admin.site.urls),
]
