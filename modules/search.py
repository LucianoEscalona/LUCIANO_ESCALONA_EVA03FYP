import json
import os

def printing(element):
    '''
    Esta funcion tiene como proposito, imprimir todos los datos de una pintura si es necesario
    ---PARAMS---
    elemt = tiene que ser el elemento de una pintura
    '''
    print(f'CODIGO: {element['codigo']}')
    print(f'NOMBRE: {element['nombre']}')
    print(f'TIPO: {element['tipo']}')
    print(f'VALOR: {element['valor']}')
    print(f'STOCK: {element['stock']}')
    print()


def search_json(jsonf, code):
    '''
    Esta funcion permite buscar un elemento del json para visualizarlo, a traves de un codigo
    ---PARAMS---
    jsonf = ruta hacia el archivo json
    code = codigo de busqueda valido
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
                    #BUSQUEDA POR CODIGO
                    if str(elemento['codigo']) == code:
                        printing(elemento)
                    #BUSQUEDA POR NOMBRE
                    elif elemento['nombre'] == code.upper():
                        printing(elemento)
    except:
        os.system('cls')
        print('ERROR: error inesperado, talves el codigo ingresado no era valido\n')


def search_code():
    '''
    Esta funcion le pide al usuario ingresar un codigo para buscar un elemento especifico del json
    Despues, retorna el valor del codigo ingresado
    ---PARAMS---
    no hay ningun PARAMS
    '''
    os.system('cls')
    scode = input('Ingresa el codigo de la pintura que desea buscar\n')
    if scode.isnumeric:
        return scode
    else:
        os.system('cls')
        print('ERROR: el codigo debe ser numerico\n')