import registermachine
from interface import menu

FILTROS = ['nome', 'Tipo', 'Marca', 'Valor']
TYPE_SELECT = [False, True]

def products_filter():
    print('0 - Pesquisa especifíca')
    print('1 - Pesquisa aproximada')
    pesquisa = int(input('Option: '))
    menu(FILTROS)
    chosen_filter = int(input('Escolha: '))

    registermachine.get_product_by(FILTROS[chosen_filter], TYPE_SELECT[pesquisa])


def remove_product():
    menu(FILTROS)
    chosen_filter = int(input('Escolha: '))

    registermachine.remove_product(FILTROS[chosen_filter])


def Switch(choice):
    comandos = {0: registermachine.stock_show,
                1: products_filter,
                2: registermachine.add_product,
                3: remove_product,
                4: registermachine.stock_value,
                5: registermachine.stock_amount,
                6: registermachine.create_user}

    return comandos.get(choice, exit)()
