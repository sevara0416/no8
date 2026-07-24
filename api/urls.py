from django.urls import path
from .views import LibraryListView,library_create,library_detail,library_update,library_delete,RegisterAPIView,ProfileAPIView,LogoutAPIView
from rest_framework_simplejwt.views import(TokenObtainPairView, TokenRefreshView)

urlpatterns=[
    path("librarys/", LibraryListView),
    path("librarys/create/", library_create),
    path("librarys/<int:pk>", library_detail),
    path("librarys/update/<int:pk>", library_update),
    path("librarys/delete/<int:pk>", library_delete),
    path("register/", RegisterAPIView.as_view()),
    path("profile/", ProfileAPIView.as_view()),
    path("login/", TokenObtainPairView.as_view()),
    path("refresh/", TokenRefreshView.as_view()),
    path("logout/", LogoutAPIView.as_view()),
]

