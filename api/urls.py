from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LibraryModelViewSet

router = DefaultRouter()

router.register("library",LibraryModelViewSet)

urlpatterns=[
    path("", include(router.urls)),
]