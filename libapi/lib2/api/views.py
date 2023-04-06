from django.shortcuts import render
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate, login
from rest_framework.permissions import IsAdminUser



# Create your views here.

class StudentAPI(APIView):
    def get(self, request,pk=None, fromat=None):
        id = pk
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)

        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    # def put(self, request, pk, format=None):
    #     id = pk
    #     stu = Student.objects.get(pk=id)
    #     serializer = StudentSerializer(stu, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({'msg':'Complete Data Updated'})
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def patch(sefl, request, pk, format=None):
    #     id = pk
    #     stu = Student.objects.get(pk=id)
    #     serializer = StudentSerializer(stu, data=request.data, partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({'msg':'Partial Data Updated'})
    #     return Response(serializer.errors)
    # def delete(self, request, pk, fromat=None):
    #     id = pk
    #     stu = Student.objects.get(pk=id)
    #     stu.delete()
    #     return Response({'msg':'Data Deleted'})
    
#library view

class LibraryAPI(APIView):
    def get(self, request,pk=None, fromat=None):
        id = pk
        if id is not None:
            lib = Library.objects.get(id=id)
            serializer = LibrarySerializer(lib)
            return Response(serializer.data)

        lib = Library.objects.all()
        serializer = LibrarySerializer(lib, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = LibrarySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

# login view

@api_view(['POST'])
def login_api(request):
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
        user = authenticate(request, username=serializer.validated_data['username'], password=serializer.validated_data['password'])
        if user is not None:
            login(request, user)
            return Response({'message': 'Login successful.'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Invalid credentials.'}, status=status.HTTP_401_UNAUTHORIZED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class IssuedBooksAPI(APIView):
    def get(self, request, format=None):
        issued_books = IssuedBook.objects.all()
        serializer = IssuedBookSerializer(issued_books, many=True)
        return Response(serializer.data)
    
class IssuedBooksAPI(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request, format=None):
        issued_books = IssuedBook.objects.all()
        serializer = IssuedBookSerializer(issued_books, many=True)
        return Response(serializer.data)
