from django.shortcuts import render
from .models import Library
from rest_framework import viewsets
from .serializers import LibrarySerializers
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(["GET"])
def LibraryListView(request):
    Librarys = Library.objects.all()
    serializer= LibrarySerializers(Librarys, many=True)
    return Response(serializer.data)

@api_view(["GET","POST"])
def library_create(request):
    if request.method == "GET":
        return Response({"message":"POST rewuest yuborn"})
    serializer = LibrarySerializers(data = request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def library_detail(request, pk):
    librarys=Library.objects.get(pk=pk)
    serializer=LibrarySerializers(librarys)
    return Response(serializer.data)

@api_view(["PATCH","PUT"])
def library_update(request, pk):
    librarys= Library.objects.get(pk=pk)
    if request.method == "PUT":
        serializer= LibrarySerializers(librarys, data=serializer.data)
    else:
        serializer = LibrarySerializers(librarys, data=request.data, partial=True)

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
