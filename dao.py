import mysql.connector
from mysql.connector import errorcode

try:
    db_connection = mysql.connector.connect(host='localhost', user='root', password='321abd4567', database='adorocinema')
    print("Database connection made!")
except mysql.connector.Error as error:
    if error.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database doesn't exist")
    elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("User name or password is wrong")
    else:
        print(error)


def salvar(nome, lancamento, duracao, categorias, descricao):
    cursor = db_connection.cursor()
    sql = "INSERT INTO filmes (Nome, Lancamento, Duracao, Categorias, Descricao) VALUES (%s, %s, %s, %s, %s)"
    values = (f"{nome}", f"{lancamento}", f"{duracao}", f"{categorias}", f"{descricao}")
    cursor.execute(sql, values)
    cursor.close()
    db_connection.commit()


def desconectar_banco():
    print("Database disconnection made!")
    return db_connection.close()
