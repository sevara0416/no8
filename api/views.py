from django.shortcuts import render
from .models import Library, CustomUser
from rest_framework import viewsets
from .serializers import LibrarySerializer, RegisterSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView

class RegisterAPIView(generics.CreateAPIView):
    serializer_class=RegisterSerializer

class ProfileAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        return Response({"username":request.user.username, "email":request.user.email,})

class LogoutAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def library(self, request):
        try:
            refresh_token=request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response({"message":"Logout seccessfil"}, status=status.HTTP_205_RESET_CONTENT)
        except Exception:
            return Response({"error":"Invalid refresh token"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def LibraryListView(request):
    Librarys = Library.objects.all()
    serializer= LibrarySerializer(Librarys, many=True)
    return Response(serializer.data)

@api_view(["GET","POST"])
def library_create(request):
    if request.method == "GET":
        return Response({"message":"POST rewuest yuborn"})
    serializer = LibrarySerializer(data = request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def library_detail(request, pk):
    librarys=Library.objects.get(pk=pk)
    serializer=LibrarySerializer(librarys)
    return Response(serializer.data)

@api_view(["PATCH","PUT"])
def library_update(request, pk):
    librarys= Library.objects.get(pk=pk)
    if request.method == "PUT":
        serializer= LibrarySerializer(librarys, data=serializer.data)
    else:
        serializer = LibrarySerializer(librarys, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["DELETE"])
def library_delete(request, pk):
    librarys= Library.objects.get(pk=pk)
    librarys.delete()
    return Response({"message":"library ochirildi"},status=status.HTTP_204_NO_CONTENT)




# # Create your views here.
# class LibraryModelViewSet(viewsets.ModelViewSet):
#     queryset = Library.objects.all()
#     serializer_class= LibrarySerializers
