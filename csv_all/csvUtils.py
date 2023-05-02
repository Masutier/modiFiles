import os
import pandas as pd


def cleanHeads(inputFile, endDir, namefile):
    df = pd.read_csv(inputFile, low_memory=False)
    df.columns = [x.upper().replace(" ","_").replace("-","_").replace("$","").replace("?","").replace("%","").replace(".","") \
            .replace("Á","A").replace("É","E").replace("Í","I").replace("Ó","O").replace("Ú","Ú")
            .replace("@","").replace("#","").replace(r"/","").replace("\\","").replace(r"(","")
            .replace(")","") for x in df.columns]
    cleanFile = df.to_csv(endDir + '/' + namefile, index=False)
    return cleanFile


def divideCsv(inputFile, endDir, filenamex, chunk, clean):
    csvChunks = []
    batchNum = 1

    for chunk in pd.read_csv(inputFile, chunksize=int(chunk)):
        if clean == "clean":
            chunk.columns = [x.upper().replace(" ","_").replace("-","_").replace("$","").replace("?","").replace("%","").replace(".","") \
                .replace("Á","A").replace("É","E").replace("Í","I").replace("Ó","O").replace("Ú","Ú")
                .replace("@","").replace("#","").replace(r"/","").replace("\\","").replace(r"(","")
                .replace(")","") for x in chunk.columns]
        chunk.to_csv(endDir + "/" +  filenamex + "_" + str(batchNum) + ".csv", index=False, header=True)
        batchNum += 1
        csvChunks.append(filenamex + "_" + str(batchNum) + ".csv")
    return csvChunks
