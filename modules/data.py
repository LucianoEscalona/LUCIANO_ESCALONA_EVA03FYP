from pathlib import Path

home = Path(__file__).parent.parent
rutaj = Path(home/'base.json')
rutac = Path(home/'mandarina.csv')

menup = ['Ver listado de Pinturas',
         'Buscar Pintura',
         'Agregar Pintura',
         'Eliminar Pintura',
         'Exportar Pintura'
        ]