from django.contrib import admin
from django.urls import path
from api import views
from api.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentapi/', views.StudentAPI.as_view()),
    path('studentapi/<int:pk>/', views.StudentAPI.as_view()),
    path('libraryapi/', views.LibraryAPI.as_view()),
    # path('libraryapi/<int:pk>/', views.LibraryAPI.as_view()),
    path('login/', login_api, name='login_api'),
    path('issuedbooksapi/', views.IssuedBooksAPI.as_view()),
]
