from django.urls import path
# from .views import login_api
# from api import views 
# from . import views
from api.views import *


urlpatterns = [
    path('login/', login_api, name='login_api'),
]
