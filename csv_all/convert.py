import pandas as pd


def csvToXlsx(inputxFile, endDir, filenamex, separator):
    df = pd.read_csv(inputxFile, low_memory=False, sep=separator)
    excelFile = df.to_excel(endDir + '/' + filenamex + ".xlsx", index=False, header=True)
    return excelFile


def csvToJson(inputxFile, endDir, filenamex, jsonType, compress):
    #df = pd.read_csv(inputFile, low_memory=False)
    jsonFilex = filenamex + ".json"

    if jsonType == 'jsonType':
        # RECORDS "ORIENT"
        jsonFile = "orient_" + jsonFilex
        output = df.to_json(endDir + '/' + jsonFile, indent=2, orient='records')
    else:
        # COLUMNS
        jsonFile = "columns_" + jsonFilex
        output = df.to_json(endDir + '/' + jsonFile, indent=2)

    # COMPRESS
    if compress == 'compress':
        jsonFileComp = "compressed_" + jsonFilex + ".gz"
        output = df.to_json(endDir + '/' + jsonFileComp, indent=2, orient='records', compression='gzip')
    else:
        jsonFileComp = []

    return jsonFile, jsonFileComp

