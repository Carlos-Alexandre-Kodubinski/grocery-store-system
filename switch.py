import db_functions
from menu_format import menu

FILTROS = ['nome', 'Tipo', 'Marca', 'Valor']
TYPE_SELECT = [False, True]

def products_filter():
    print('0 - Pesquisa especifíca')
    print('1 - Pesquisa aproximada')
    pesquisa = TYPE_SELECT[int(input('Option: '))]
    menu(FILTROS)
    option = FILTROS[int(input('Escolha: '))]

    db_functions.get_product_by(option, pesquisa)


def remove_product():
    menu(FILTROS)
    option = FILTROS[int(input('Escolha: '))]

    db_functions.remove_product(option)


def Switch(choice):
    comandos = {0: db_functions.stock_show,
                1: products_filter,
                2: db_functions.add_product,
                3: remove_product,
                4: db_functions.update,
                5: db_functions.stock_value,
                6: db_functions.stock_amount,
                7: db_functions.create_user}


    return comandos.get(choice, exit)()
