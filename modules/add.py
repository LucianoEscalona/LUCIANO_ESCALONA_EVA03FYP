import os
import json

def add_json(jsonf):
    '''
    Esta funcion permite agregar datos a un archivo json, si este archivo no existe
    lo creara.
    ---PARAMS---
    jsonf = ruta del archivo json
    '''
    os.system('cls')
    if not jsonf.exists():
        jsonf.touch()
        print('El archivo json no existia, pero ya se ha creado\n')
    if jsonf.stat().st_size == 0:
        json_file = []
        codigo = 380560
    else:
        with open(jsonf, mode='r') as stream:
            json_file = json.load(stream)
            codigo = []
            for pintura in json_file:
                codigo.append(pintura['codigo'])
            codigo = max(codigo) + 1
    
    #NOMBRE
    while True:
        print('Ingrese el nombre (color) de la pintura\n')
        nombre = input('NOMBRE: ').upper()
        ans = input(f'NOMBRE: {nombre}, el dato ingresado es correcto?\nPresione -1- para confirmar\n')
        if ans == '1':
            os.system('cls')
            break
        else:
            os.system('cls')
    #TIPO
    while True:
        print('Ingrese el tipo de pintura (ACRILICO o LATEX)\n')
        tipo = input('TIPO: ').upper()
        ltipo = ['ACRILICO', 'LATEX']
        ans = input(f'TIPO: {tipo}, el dato ingresado es correcto?\nPresione -1- para confirmar\n')
        if ans == '1' and tipo in ltipo:
            os.system('cls')
            break
        else:
            os.system('cls')

    #VALOR
    while True:
        print('Ingrese el valor de la pintura\n')
        valor = input('VALOR: ')
        ans = input(f'VALOR: {valor}, el dato ingresado es correcto?\nPresione -1- para confirmar\n')
        if ans == '1' and valor.isnumeric():
            valor = int(valor)
            os.system('cls')
            break
        else:
            os.system('cls')
    
    #STOCK
    while True:
        print('Ingrese el stock de la pintura\n')
        stock = input('STOCK: ')
        ans = input(f'STOCK: {stock}, el dato ingresado es correcto?\nPresione -1- para confirmar\n')
        if ans == '1' and stock.isnumeric():
            stock = int(stock)
            os.system('cls')
            break
        else:
            os.system('cls')
    
    data = {'codigo': codigo,
            'nombre': nombre,
            'tipo': tipo,
            'valor': valor,
            'stock': stock
            }
    json_file.append(data)
    with open(jsonf, mode='w') as stream:
        json.dump(json_file, stream)
        os.system('cls')
        print('Los datos se han guardado exitosamente\n')