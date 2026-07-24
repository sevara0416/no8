from rest_framework import serializers
from .models import Library
from django.contrib.auth import get_user_model
User=get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only= True)

    class Meta:
        model=User
        fields = ["id","username","email","password","age","phone_number"]
        read_only_fields=["created_at"]

    def create(self, validated_data):
        user= User.objects.create_user(
            username=self.validated_data["username"],
            email=self.validated_data["email"],
            password=self.validated_data["password"],
            age=self.validated_data["age"],
            phone_number=self.validated_data["phone_number"],
        )
        return user

class LibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model =Library
        fields=["id","name","price","pages","author","created_at"]
        read_only_fields= ["created_at"]

