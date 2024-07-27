"""
ESTA ES EL CODIGO PARA EJECUTARLO DIRECTAMENTE DESDE GOOGLE COLAB
from google.colab import drive
drive.mount('/content/drive')

# Para obtener el encoding del csv (pues no se encontraba en utf-8)
import chardet
rawdata = open("/content/drive/MyDrive/python-basico/datasets/characters-hp.csv", 'rb').read()
result = chardet.detect(rawdata)
charenc = result['encoding']
print(charenc)
"""

# Para obtener el encoding del csv (pues no se encontraba en utf-8)
import chardet    
rawdata = open("CargaArchivosPython\ArchivosCSV\charactershp-220809-170900.csv", 'rb').read()
result = chardet.detect(rawdata)
charenc = result['encoding']
print(charenc)

import pandas as pd
hp_df = pd.read_csv("CargaArchivosPython\ArchivosCSV\charactershp-220809-170900.csv",
                    sep = ";", encoding = "Windows-1252")