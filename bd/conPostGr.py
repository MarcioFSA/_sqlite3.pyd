
import psycopg2
from psycopg2 import errors


host='localhost'
user='postgres'
password= 'megatrends'
dbname='Reserva_treinamento'
# sslmode = 'require'

def connectarbd():
    try:
        conn_string = 'host ={0} user={1} dbname={2} password={3}'.format(host, user, dbname, password)
        conn = psycopg2.connect(conn_string)
        return conn
        print(conn)

    except errors as e:
        print("Erro ao conectar ao Banco de Dados:" + str(e))


print('Conectado')
