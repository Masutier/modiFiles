import os
import pandas as pd


def cleanHeads(inputFile, endDir, namefile):
    df = pd.read_excel(inputFile, sheet_name='Employees')
    df.columns = [x.upper().replace(" ","_").replace("-","_").replace("$","").replace("?","").replace("%","").replace(".","") \
            .replace("Á","A").replace("É","E").replace("Í","I").replace("Ó","O").replace("Ú","Ú")
            .replace("@","").replace("#","").replace(r"/","").replace("\\","").replace(r"(","")
            .replace(")","") for x in df.columns]
    cleanFile = df.to_csv(endDir + '/' + namefile, index=False)
    return cleanFile
