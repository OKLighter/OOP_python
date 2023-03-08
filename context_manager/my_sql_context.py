"""
Пример использования менеджера контекста
"""
import os
import contextlib
import mysql.connector


@contextlib.contextmanager
def get_mysql_conn(db):
    """
    Context manager to automatically close DB connection.
    We retrieve credentials from Environment variables
    """
    conn = mysql.connector.connect(
        host=os.environ.get('MYSQL_HOST'),
        user=os.environ.get('MYSQL_USER'),
        password=os.environ.get('MYSQL_PWD'),
        database=db
    )

    try:
        yield conn
    finally:
        conn.close()


"""
Обратите внимание на блок try-finally.
В нем мы пытаемся вернуть объект conn в менеджер контекста блока with и вызываем метод .close()
"""
