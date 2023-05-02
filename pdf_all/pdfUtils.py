import os
import pandas as pd
import math
from django.conf import settings
from PyPDF2 import PdfWriter, PdfReader, PdfFileReader
from pdf2image import convert_from_bytes

origen_path = "/home/gabriel/Downloads/"
filepath = os.path.join(settings.BASE_DIR, "FILES/pdf/")


def dividePdf(origen_path, nameFile, endDir, newName, chunk, divide, extract):
    # open file and check num pages (origen_path, nameFile )
    with open(origen_path + "/" + nameFile, "rb") as f:
        reader = PdfFileReader(f)
        pagesAll = len(reader.pages)

        if pagesAll <= chunk:
            messages.success(request, "The .pdf is smaller than the size you ask for, It was not divided")
            return redirect("home")
        else:
            topages = pagesAll/chunk
            pagesround = math.floor(topages) # round down the number
            diference = topages - pagesround

            if diference != 0:
                pagesround += 1
            chunk1 = 1
            chunk2 = chunk + 1
            count = 0
            count2 = 0

            for i in range(pagesround):
                part = "part" + str(i)
                part = PdfWriter()
                first = list(range(chunk1, chunk2))

                for page in range(pagesAll):
                    if page in first:
                        count += 1
                        part.add_page(reader.pages[page])

                piece = endDir + "/" + newName + "_part" + str(i) + ".pdf"

                with open(piece, "wb") as f2:
                    part.write(f2)

                if extract == "extract":
                    extractjpg(piece, i, endDir, newName, count2)
                    chunk1 += chunk
                    chunk2 += chunk
                    count2 += chunk

                if divide == "notdivide":
                    os.remove(piece)


def extractjpg(piece, i, endDir, newName, count2):
    images = convert_from_bytes(open(piece, 'rb').read())
    for imag in images:
        count2 += 1
        if imag.width > 1000:
            new_img = (1000, None)
            imag.save(endDir + "/" + newName + "_" + str(count2) + '.jpg', 'JPEG', quality=95)
        else:
            imag.save(endDir + "/" + newName + "_" + str(count2) + '.jpg', 'JPEG', quality=95)
