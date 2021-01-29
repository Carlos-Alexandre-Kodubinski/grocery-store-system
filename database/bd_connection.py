from mysql.connector import connect
from contextlib import contextmanager

parametros = dict(
    host='192.168.1.23',
    user='carlos',
    passwd= 'carlos123',
    port= 3306,
    database= 'mercado',
    auth_plugin= 'mysql_native_password', use_unicode=True, charset='utf8'
    )

@contextmanager
def new_connection():
    conexao = connect(**parametros)
    try:
        yield conexao
    finally:
        if (conexao and conexao.is_connected()):
            conexao.close()
