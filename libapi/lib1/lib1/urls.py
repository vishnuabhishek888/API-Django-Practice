from django.urls import path, include
from rest_framework import routers
from api.views import *
router = routers.DefaultRouter()
router.register('students', StudentViewSet)
router.register('library',LibraryViewSet)


urlpatterns = [
    path('', include(router.urls)),
]

