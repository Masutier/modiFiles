import os
import pandas as pd
import sqlite3 as sql
from django.conf import settings


# Crear la Base de Datos
def createDB():
    conn=sql.connect(os.path.join(settings.BASE_DIR, "senadlakedb"))
    conn.commit()
    conn.close()


def loadTodbsql(inputFile, filenamex):
    # Limpiar los nombres de columnas
    df = pd.read_csv(inputFile, low_memory=False)
    df.columns = [x.upper().replace(" ","_").replace("-","_").replace("$","").replace("?","").replace("%","").replace(".","")
        .replace("Á","A").replace("É","E").replace("Í","I").replace("Ó","O").replace("Ú","Ú")
        .replace("@","").replace("#","").replace(r"/","").replace("\\","").replace(r"(","").replace(")","") for x in df.columns]

    conn=sql.connect(os.path.join(settings.BASE_DIR, "senadlake.db"))
    df.to_sql(name=filenamex, con=conn, if_exists="append", index=False)
    conn.close()
