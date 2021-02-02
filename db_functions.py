from database.bd_connection import new_connection
from mysql.connector.errors import ProgrammingError
from menu_format import menu


def stock_show():
    """
    show all database
    param none
    return none
    """
    sql = 'select * from produtos'

    with new_connection() as conexao:
        try: 
            cursor = conexao.cursor()
            cursor.execute(sql)
        except ProgrammingError as e:
            print(f'ERROR: {e.msg}')
        else:
            for i in cursor.fetchall():
                print(f'ID: {i[0]:3}, NOME: {i[1]:25} MARCA: {i[2]:15} TIPO: {i[3]:20} VALOR: {i[4]}')


def add_product():
    """
    adiciona um produto ao estoque
    :param projuct: produto que será adicionado
    :return: sem retorno
    """

    sql = 'insert into produtos (nome, marca, tipo, valor) values (%s, %s, %s, %s)'
    parametros = {'nome':'', 'marca':'', 'tipo':'', 'valor':''}
    for keys in parametros.keys():
        while parametros[keys] == '':
            parametros[keys] = input(f'{keys}: ').strip().lower()
            if keys == 'valor':
                try:
                    parametros[keys] = int(parametros[keys])
                except:
                    parametros[keys] = ''
    with new_connection() as conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute(sql, tuple(parametros.values()))
            conexao.commit()
        except ProgrammingError as e:
            print(f'ERROR: {e.msg}')
        else:
            print('Produto adicionado com sucesso!')


def get_product_by(key, like=False):
    """
    Pega os produtos por um tipo específico
    :param key: O tipo passado
    :return: sem retorno
    """
    sql = f'select * from produtos where {key} = %s'\
         if not like else f'select * from produtos where {key} like %s'
    campo = (input(f'{key.upper()}: ').strip().lower(), ) \
        if not like else (f'%{input(f"{key.upper()}: ").strip().lower()}%', )

    with new_connection() as conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute(sql, campo)
        except ProgrammingError as e:
            print(f'ERRO: {e.msg}')
        else:
            for i in cursor:
                print(f'ID: {i[0]:3}, NOME: {i[1]:25} MARCA: {i[2]:15} TIPO: {i[3]:20} VALOR: {i[4]}')


def remove_product(key):
    sql = f'delete from produtos where {key} = %s'
    campo = (input(f'{key.upper()}: ').strip().lower(), )
    
    with new_connection() as conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute(sql, campo)
            conexao.commit()
        except ProgrammingError as e:
            print(f'ERROR: {e.msg}')
        else:
            print(f'{cursor.rowcount} linha(s) afetadas.')


def stock_value():
    """
    soma o valor total do estoque
    :return: total do estoque
    """
    
    sql = 'select sum(valor) as soma from produtos'

    with new_connection() as conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute(sql)
            total = cursor.fetchone()[0]
        except ProgrammingError as e:
            print(f'ERROR: {e.msg}')
        else:
            print(f'O valor do estoque é de R${total},00.')


def stock_amount():
    """
    Quantidades de produtos no estoque
    :return: retorna quantidade de produtos
    """
    sql = 'select count(*) from produtos'

    with new_connection() as conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute(sql)
            total_linha = cursor.fetchone()[0]
        except ProgrammingError as e:
            print(f'ERROR: {e.msg}')
        else:
            print(f'Existem {total_linha} registros no banco de dados.')


def create_user():
    sql = 'insert into users (nome, senha) value (%s, %s)'
    args = (
        input('Name: ').strip().lower(),
        input('Password: ').strip().lower()
    )

    with new_connection() as conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute(sql, args)
            conexao.commit()
        except ProgrammingError as e:
            print(f'ERROR: {e.msg}')
        else:
            print('Um novo user foi criado')

def update():
    def get_field(text):
        campos = ['nome', 'marca', 'tipo', 'valor']

        print('-'*50)
        print(text)
        menu(campos)
        index_campos = int(input('Campo: '))
        return campos[index_campos]
    

    update_field = get_field('Atualizar Qual campo')
    new_value_field = input('Novo valor do campo: ')
    filter_field = get_field('Usar qual campo para filtrar?')
    value_filter_field = input('Valor do filtro: ')

    sql = f'UPDATE produtos SET {update_field} = %s WHERE {filter_field} = %s'

    args = (new_value_field, value_filter_field)

    with new_connection() as conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute(sql, args)
            conexao.commit()
        except ProgrammingError as e:
            print(f'ERROR: {e.msg}')
        else:
            print(f'Banco atualizado, {cursor.rowcount} linha(s) alterada(s)')

