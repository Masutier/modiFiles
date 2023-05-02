from django.urls import path, include
from .views import *

urlpatterns = [
    path('pdfAllFiles', pdfAllFiles, name="pdfAllFiles"),

]
