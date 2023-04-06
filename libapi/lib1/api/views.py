from rest_framework import viewsets
from .models import *
from .serializers import * 
# from rest_framework.authentication import BasicAuthentication
# from rest_framework.permissions import IsAuthenticated

# Create your views here.

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class LibraryViewSet(viewsets.ModelViewSet):
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer

     