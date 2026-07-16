from django.shortcuts import render
from .models import Library
from rest_framework import viewsets
from .serializers import LibrarySerializers

# Create your views here.
class LibraryModelViewSet(viewsets.ModelViewSet):
    queryset = Library.objects.all()
    serializer_class= LibrarySerializers
