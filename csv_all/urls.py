from django.urls import path, include
from .views import *

urlpatterns = [
    path('csvAllFiles', csvAllFiles, name="csvAllFiles"),

]
