import json
import os

def remove_json(jsonf, code):
    '''
    Esta funcion sirve para remover datos de un archivo json a traves de un codigo
    ---PARAMS---
    jsonf = ruta hacia el archivo json
    code = codigo valido para borrar un elemento
    '''
    os.system('cls')
    try:
        if not jsonf.exists():
            print('El archivo json no existe\n')
        elif jsonf.stat().st_size == 0:
            print('El archivo esta vacio\n')
        elif code == None:
            print('El codigo no tiene ningun valor asignado\n')
        else:
            with open(jsonf, mode='r') as stream:
                json_file = json.load(stream)
                for elemento in json_file:
                    if str(elemento['codigo']) == code:
                        json_file.remove(elemento)
                        os.system('cls')
                        print('Elemento borrado con exito\n')
            with open(jsonf, mode='w') as stream:
                json.dump(json_file, stream)
    except:
        os.system('cls')
        print('ERROR: error inesperado, talves el codigo ingresado no era valido\n')


def removal_code():
    '''
    Esta funcion le pide al usuario ingresar un codigo para eliminar un elemento del json
    Despues, retorna el valor del codigo ingresado
    ---PARAMS---
    no hay ningun PARAMS
    '''
    os.system('cls')
    rcode = input('Ingresa el codigo de la pintura a eliminar\n')
    if rcode.isnumeric:
        return rcode
    else:
        os.system('cls')
        print('ERROR: el codigo debe ser numerico\n')