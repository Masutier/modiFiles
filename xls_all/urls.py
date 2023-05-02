from django.urls import path, include
from .views import *

urlpatterns = [
    path('xlsxFirst', xlsxFirst, name="xlsxFirst"),
    path('xlsAllFiles', xlsAllFiles, name="xlsAllFiles"),
    

]
xlsxFirst