import sqlite3

class UncommittedTask_DATA:
    def __init__(self, db_path):
        self.db_path = db_path # variable que indica la ubicacion de la base de datos SQLite -> es una ruta al archivo
        self.initialize_db() # efectua la creacion de la tabla

    def initialize_db(self): # Crea la tabla si no existe al iniciar el programa
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS UncommittedTask (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                date_created TEXT NOT NULL
            )
        ''')
        conn.commit()
        conn.close()

    def connect(self): # al llamar a este metodo, se abre una conexion con la base de datos, la cual luego debe ser cerrada
        return sqlite3.connect(self.db_path) # conecta con la base de datos especificada en db_path
        # si el archivo no existe, se crea

    def addTask(self, taskName):
        conn = self.connect()
        cursor = conn.cursor() # el cursor es un objeto que permite ejecutar comandos SQL sobre una base de datos abierta
        cursor.execute('''
            INSERT INTO UncommittedTask (name, date_created)
            VALUES (?, datetime('now'))
        ''', (taskName,))
        conn.commit() # guarda los cambios hechos
        conn.close() # cierra la conexion a la base de datos

    def get_tasks(self): # obtiene los datos de las tasks
        conn = self.connect() # conectar con base de datos
        cursor = conn.cursor() # llamar al cursor que permite ejecutar los comandos
        cursor.execute('SELECT id, name, date_created FROM UncommittedTask') # usar "SELECT" que permite elegir ciertos datos de una tabla
        tasks = cursor.fetchall() # recoge todas las filas de la ultima instruccion ejecutada por el cursor
        # retorna una lista de tuplas, donde cada tupla representa una fila de la base de datos que coincidió con la consulta SELECT
        conn.close()
        return tasks # devuelve la lista de tuplas
    
    def deleteTask(self, taskName):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute('''
            DELETE FROM UncommittedTask WHERE name = ?
        ''', (taskName,)) # se debe pasar como tupla para cumplir con requisitos de SQLite
        conn.commit()
        conn.close()

uncommittedTask_DATA = UncommittedTask_DATA("UncommittedTask.db")


