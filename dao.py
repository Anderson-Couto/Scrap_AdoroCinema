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


def salvar_nome_desc(nome, descricao):
    cursor = db_connection.cursor()
    sql = "INSERT INTO filmes (Nome, Descricao) VALUES (%s, %s)"
    values = (f"{nome}", f"{descricao}")
    cursor.execute(sql, values)
    cursor.close()
    db_connection.commit()


def desconectar_banco():
    print("Database disconnection made!")
    return db_connection.close()
