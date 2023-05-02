import os
import json
import pandas as pd
from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, redirect
from modiFiles.rootutils import pickcss, newFolder
from .xlsUtils import cleanHeads

origen_path = "/home/gabriel/Downloads/"
filepath = os.path.join(settings.BASE_DIR, "FILES/xlsx/")


def xlsxFirst(request):

    if request.method == "POST":
        inputFile = request.POST['inputFile']
        df = pd.ExcelFile(origen_path + inputFile)
        sheet_names = df.sheet_names

        context={"title": "XLSX All", "inputFile":inputFile, "sheet_names":sheet_names}
        return render(request, 'xls_all/xlsLoad.html', context)

    context={"title": "XLSX All"}
    return render(request, 'xls_all/xlsFirst.html', context)


def xlsAllFiles(request):

    if request.method == 'POST':
        inputFile = request.POST['inputFile']
        sheetName = request.POST['sheetName']
        separator = request.POST['separator']
        newfolder = request.POST['newfolder']
        clean = request.POST['clean']
        toCsv = request.POST['toCsv']
        json = request.POST['json']
        jsonType = request.POST['jsonType']
        compress = request.POST['compress']
        loadtosql = request.POST['loadtosql']

        print('inputFile', inputFile)
        filenamex = inputFile.split('.')
        print('filenamex', filenamex)
        print('sheetName', sheetName)

        if filenamex[-1] != "xlsx":
            messages.success(request, "The file you enter is not an excel file, please check the file and try again")
            return redirect('home')

        # CREATE FOLDER
        endDir = newFolder(filepath, newfolder, filenamex[0])

        print('endDir', endDir)

        messages.success(request, "The file xxxxxxxxvvvvvvvvv")
        return redirect('home')



    context={"title": "XLSX All", "sheet_names":sheet_names}
    return render(request, 'xls_all/xlsLoad.html', context)
