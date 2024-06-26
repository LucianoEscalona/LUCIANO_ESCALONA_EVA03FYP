import json
import os

def build_mm(lista):
    '''
    Esta funcion costruye una lista a partir de un elemento iterable
    ---PARAMS---
    lista = debe ser un elemento iterable/una lista
    '''
    for i, o in enumerate(lista):
        print(f'{i + 1}. {o}')


def opt_code():
    '''
    Esta funcion recoge un numero para navegar a traves del menu principal
    ---PARAMS---
    no hay ningun params
    '''
    opt = input('Que accion desea realizar?\n')
    return opt


def build_json(jsonf):
    os.system('cls')
    if not jsonf.exists():
        print('El archivo json no existe\n')
    elif jsonf.stat().st_size == 0:
        print('El archivo esta vacio\n')
    else:
        with open(jsonf, mode='r') as stream:
            json_file = json.load(stream)
            for elemento in json_file:
                    print(f'CODIGO: {elemento['codigo']}')
                    print(f'NOMBRE: {elemento['nombre']}')
                    print()