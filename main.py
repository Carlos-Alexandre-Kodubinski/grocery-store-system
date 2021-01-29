#!venv/bin/python
from commands import Switch
from interface import menu
from database.bd_connection import new_connection
from mysql.connector.errors import ProgrammingError
from last_user import data


TEXT_MENU = ['Ver Produtos em estoque', 'Procurar produto',
             'Adicionar produto', 'Remover Produto', 'Valor do estoque',
             'Quantidade de produtos', 'Criar users']

def main():
    while True:
        menu(TEXT_MENU)
        chosen_option = int(input('Opção: '))

        Switch(chosen_option)


def authentication():
    sql = 'select nome, senha from users'

    print('Write exit to close the program.')
    name = input('USER: ').strip().lower()
    if name == 'exit':
        exit()
        
    password = input('PASSAWORD: ').strip().lower()
    if password == 'exit':
        exit()
    
    with new_connection() as conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute(sql)
            users = cursor.fetchall()
        except ProgrammingError as e:
            print(f'ERROR: {e.msg}')
        else:
            for u in users:
                if (name, password) == u:
                    print('access authorized!')
                    return True

            print('User or password incorrect!')
            return False


def start():
    while True:
        if authentication():
            main()


if __name__ == '__main__':
    start()
