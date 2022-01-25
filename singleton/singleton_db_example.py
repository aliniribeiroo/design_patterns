"""
    Para um bom design de um serviço que acessa um banco de dados em nuvem,
    precisamos prestar atenção nos sehguintes pontos:

    - Consistência entre operações no banco de dados. Uma operação não deve resultar em conflito com as outras;
    - A utilização de memória e CPU deve estar otimizada para o tratamento de várias operações no banco de dados.

    Quando há muitas aplicações se conectando com o banco de dados o mais indicado é
     utilizar um pool de copnexões, e não singleton.


"""

import sqlite3


class MetaSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Database(metaclass=MetaSingleton):
    connection = None

    def connect(self):
        if self.connection is None:
            self.connection = sqlite3.connect("db.sqlite3")
            self.cursorobj = self.connection.cursor()
        return self.cursorobj


db1 = Database().connect()
db2 = Database().connect()

print("Database Objects DB1", db1)
print("Database Objects DB2", db2)
