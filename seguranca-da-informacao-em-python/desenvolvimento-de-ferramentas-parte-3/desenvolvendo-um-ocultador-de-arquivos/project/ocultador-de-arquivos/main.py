import ctypes
import os

# Windows
atributo_ocultar = 0x02

retorno = ctypes.windll.kernel32.SetFileAttributesW("ocultar.txt", atributo_ocultar)

if retorno:
    print("Arquivo foi ocultado.")
else:
    print("Arquivo nõa foi ocultado")

# Linux
arquivo = "ocultar.txt"

os.rename(arquivo, f".{arquivo}")
