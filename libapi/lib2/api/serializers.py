from rest_framework import serializers
from .models import *

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class LibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Library
        fields = '__all__'


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

class IssuedBookSerializer(serializers.ModelSerializer):
    student = StudentSerializer()
    library = LibrarySerializer()

    class Meta:
        model = IssuedBook
        fields = '__all__'

    def create(self, validated_data):
        # Update the quantity of the Library model when a book is issued
        library = validated_data['library']
        library.quantity -= validated_data['quantity']
        library.save()

        # Create the IssuedBook object
        issued_book = IssuedBook.objects.create(**validated_data)
        return issued_book



