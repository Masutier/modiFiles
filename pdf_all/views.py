import os
import csv, json
import pandas as pd
import math
from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, redirect
from modiFiles.rootutils import newFolder
from PyPDF2 import PdfWriter, PdfReader, PdfFileReader
from .pdfUtils import dividePdf, extractjpg
from pdf2image import convert_from_bytes

origen_path = "/home/gabriel/Downloads/"
filepath = os.path.join(settings.BASE_DIR, "FILES/pdf/")


def pdfAllFiles(request):

    if request.method == 'POST':
        inputFile = request.FILES['inputFile']
        newfoldername = request.POST['newfoldername']
        newfilename = request.POST['newfilename']
        divide = request.POST['divide']
        chunk = request.POST['chunk']
        extract = request.POST['extract']
        nameFile = inputFile.name

        # define file name
        if newfilename:
            newName = newfilename
        else:
            fileNamex = nameFile.split('.')
            newName = fileNamex[0]
        
        # verify type of file
        if filenamex[-1] != "pdf":
            messages.success(request, "The file is not a .pdf, please check file and try again")
            return redirect('home')

        # define folder name
        endDir = newFolder(filepath, newfoldername, newName)

        # define chunk size
        if not chunk:
            chunk = 100
        else:
            chunk = int(chunk)

        # DIVIDE pdf NOT EXTRACT to jpg
        if divide == "divide" and extract == "notextract":
            dividePdf(origen_path, nameFile, endDir, newName, chunk, divide, extract)
            messages.success(request, "The .pdf was divided successfuly")
            return redirect('home')

        # DIVIDE pdf AND EXTRACT to jpg
        if divide == "divide" and extract == "extract":
            dividePdf(origen_path, nameFile, endDir, newName, chunk, divide, extract)
            messages.success(request, "The .pdf was divided successfuly and .jpg's created")
            return redirect('home')

        # NOT DIVIDE pdf BUT EXTRACT jpg's
        if divide == "notdivide" and extract == "extract":
            chunk = 100
            dividePdf(origen_path, nameFile, endDir, newName, chunk, divide, extract)
            messages.success(request, "The .pdf was divided successfuly and .jpg's created")
            return redirect('home')

    context={"title": "PDF All"}
    return render(request, 'pdf_all/pdfLoad.html', context)



#****************************  extract 


def extractTxt_PyPDF():
    # importing required modules
    from PyPDF2 import PdfReader
    
    # creating a pdf reader object
    reader = PdfReader('example.pdf')
    
    # printing number of pages in pdf file
    print(len(reader.pages))
    
    # getting a specific page from the pdf file
    page = reader.pages[0]
    
    # extracting text from page
    text = page.extract_text()
    print(text)


def extractTxt_PyMuPDF():
    #pip install PyMuPDF==1.16.14
    import fitz
    doc = fitz.open('sample.pdf')
    text = ""
    for page in doc:
        text += page.get_text()
    print(text)