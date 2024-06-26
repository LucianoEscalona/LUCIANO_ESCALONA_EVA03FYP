import json
import csv
import os

def export(rutaj, rutac):
    '''
    Esta funcion exporta los datos del json en un csv
    ---PARAMS---
    rutaj = ruta hacia el archivo json
    rutac = lugar donde se exportara el archivo csv
    '''
    os.system('cls')
    if not rutaj.exists():
        print('El archivo json no existe\n')
    elif rutaj.stat().st_size == 0:
        print('El archivo esta vacio\n')
    else:
        if not rutac.exists():
            rutac.touch()
        else:
            rutac.unlink()
            rutac.touch()
        with open(rutaj, mode='r') as stream:
            json_file = json.load(stream)
            for elemento in json_file:
                line = [elemento['codigo'],
                        elemento['nombre'],
                        elemento['tipo'],
                        elemento['valor'],
                        elemento['stock'],]
                with open(rutac, mode='a', newline='') as cfile:
                    write = csv.writer(cfile)
                    write.writerow(line)