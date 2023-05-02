import os
import csv, json
import pandas as pd
from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, redirect
from .csvUtils import cleanHeads, divideCsv
from .convert import csvToXlsx, csvToJson
from .csvdbs import createDB, loadTodbsql
from modiFiles.rootutils import newFolder

origen_path = "/home/gabriel/Downloads/"
filepath = os.path.join(settings.BASE_DIR, "FILES/csv/")


def csvAllFiles(request):

    if request.method == 'POST':
        inputFile = request.FILES['inputFile']
        separator = request.POST['separator']
        newfolder = request.POST['newfolder']
        divide = request.POST['divide']
        clean = request.POST['clean']
        chunk = request.POST['chunk']
        toExcel = request.POST['toExcel']
        json = request.POST['json']
        jsonType = request.POST['jsonType']
        compress = request.POST['compress']
        loadtosql = request.POST['loadtosql']

        namefile = inputFile.name
        filenamex = namefile.split('.')

        if filenamex[-1] != "csv":
            messages.success(request, "The file is not a .csv, please check file and try again")
            return redirect('home')

        # CREATE FOLDER
        endDir = newFolder(filepath, newfolder, filenamex[0])

        # DIVIDE FILE AND CLEAN
        if divide == 'divide' and clean == 'clean':
            divideCsv(inputFile, endDir, filenamex[0], chunk, clean)

        elif divide == 'divide' and clean == 'notclean':
            divideCsv(inputFile, endDir, filenamex[0], chunk, clean)

        elif divide == 'notdivide' and clean == 'clean':
            cleanFile = cleanHeads(inputFile, endDir, namefile)

        if toExcel == 'toExcel':
            excelFile = csvToXlsx(inputFile, endDir, filenamex[0], separator)
            messages.success(request, f"The .csv was conver to a .xlsx file successfully")

        if json == 'json':
            jsonFile, jsonFileComp = csvToJson(inputFile, endDir, filenamex[0], jsonType, compress)
            # Read json compressed files
            # print(pd.read_json(endDir + "/" + jsonFileComp))

        if loadtosql == 'loadtosql':
            loadTodbsql(inputFile, filenamex[0])
            
            messages.success(request, f"The .csv was loaded into a db successfully")

    context={"title": "CSV All"}
    return render(request, 'csv_all/csvLoad.html', context)
