from rest_framework.serializers import ModelSerializer
from .models import Library

class LibrarySerializers(ModelSerializer):
    class Meta:
        model =Library
        fields=["id","name","price","pages","author","created_at"]
        read_only_fields= ["id", "created_at"]