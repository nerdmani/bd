import mysql.connector

def conectar():
    mydb = mysql.connector.connect(
        host='db.cpcvu9ttx9uj.us-east-1.rds.amazonaws.com',
        user='admin',
        password='lucas123',
        database='livro'
        )
    return mydb