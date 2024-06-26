from modules.data import home, rutac, rutaj, menup
from modules.add import add_json
from modules.build import build_mm, opt_code, build_json
from modules.search import search_json, search_code
from modules.export import export
from modules.remove import remove_json, removal_code

while True:
    build_mm(menup)
    ans = opt_code()
    if ans == '1':
        build_json(rutaj)
    elif ans == '2':
        search_json(rutaj, search_code())
    elif ans == '3':
        add_json(rutaj)
    elif ans == '4':
        remove_json(rutaj, removal_code())
    elif ans == '5':
        export(rutaj, rutac)