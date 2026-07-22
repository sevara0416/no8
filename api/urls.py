from django.urls import path
# from rest_framework.routers import DefaultRouter
from .views import LibraryListView,library_create,library_detail,library_update,library_delete


urlpatterns=[
    path("librarys/", LibraryListView),
    path("librarys/create/", library_create),
    path("librarys/<int:pk>", library_detail),
    path("librarys/update/<int:pk>", library_update),
    path("librarys/delete/<int:pk>", library_delete),
]