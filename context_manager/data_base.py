"""
Менеджер контекста для открытия соединения к базе данных
"""

import sqlite3
"""
В качестве примера разберем базу данных sqlite3. 
Вот так могла выглядеть программа подключения к БД без менеджера контекста:
"""
try:
    con = sqlite3.connect("mydb.sqlite")
except sqlite3.Error as er:
    print("Error connecting to database:", er)

cur = con.cursor()
sql_query = "INSERT INTO user VALUES(?, ?)"
sql_data = ("John", "MacDonald")

try:
    cur.execute(sql_query, sql_data)
    con.commit()
except sqlite3.Error as er:
    print('SQLite error: %s' % (' '.join(er.args)))
    print("Exception class is: ", er.__class__)
    print('SQLite traceback: ')
finally:
    con.close()
#################################################################################################################
import sqlite3


class DatabaseManager:
    """
    В __enter__() мы пытаемся подключиться к базе данных. Если произойдет ошибка, мы выводим сообщение об ошибке
    и возвращаем None. Если подключение установлено успешно, мы возвращаем объект соединения.
    __exit__() закрывает соединение с базой данных в блоке try-except.
    Если соединение не было установлено, возникает исключение AttributeError.
    Если при закрытии соединения возникли другие ошибки, они отлавливаются и
    выводится сообщение об ошибке с их описанием.
    """
    def __init__(self, db_name):
        self.db_name = db_name

    def __enter__(self):
        try:
            self.conn = sqlite3.connect(self.db_name)
        except sqlite3.Error as e:
            print("Error connecting to database:", e)
            return None
        else:
            return self.conn

    def __exit__(self, exc_type, exc_value, traceback):
        try:
            self.conn.close()
        except AttributeError:
            print("Database connection not established")
        except sqlite3.Error as e:
            print("An error occurred while closing the database connection: ", e)

"""
Пример использования контекстного менеджера класса DatabaseManager:

with DatabaseManager("mydb.sqlite") as conn:
    if conn:
        cur = conn.cursor()
        sql_query = "INSERT INTO user VALUES(?, ?)"
        sql_data = ("John", "MacDonald")
        cur.execute(sql_query, sql_data)
        conn.commit()
        
В этом примере контекстный менеджер открывает базу данных "mydb.sqlite" 
и выполняет запрос на вставку записи в таблицу "user". Если произойдет ошибка при подключении к базе данных,
выводится соответствующее сообщение. Если при работе с базой данных возникнут другие ошибки,
они отлавливаются и выводится сообщение об ошибке с их описанием.
После окончания работы контекстного менеджера соединение с базой данных автоматически закрывается
"""