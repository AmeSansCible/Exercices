import sqlite3
from sqlite3 import Error

def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

connection = create_connection("C:\\Users\\racli\\PycharmProjects\\Test_mimo\\Ex_SQLite.db")

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

#Creation des tables : store the query in a string puis execute_query(connection, nom_de_la_variable)
create_students_table = """
CREATE TABLE students (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  first_name VARCHAR(30) NOT NULL,
  name VARCHAR(30) NOT NULL,
  age INTEGER,
  gender TEXT
);
"""
create_levels_table = """
CREATE TABLE levels (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  level TEXT
);
"""

create_requirements_table = """
CREATE TABLE requirements (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    level TEXT,
    row TEXT,
    column TEXT,
    seat TEXT
);
"""
create_desks_table = """
CREATE TABLE desks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    row INTEGER,
    column INTEGER,
    seat INTEGER
);
"""


execute_query(connection, create_students_table)
execute_query(connection, create_levels_table)
execute_query(connection, create_requirements_table)
execute_query(connection, create_desks_table)

#Ajouter des valeurs dans mes tableaux
create_students = """
INSERT INTO
    students (first_name, name, age, gender)
VALUES
    ('Maeva', 'Duboux', 10, 'female'),
    ('Noémie', 'Pierrot', 11, 'female'),
    ('Nathan', 'Palot', 11, 'male');
"""

create_levels = """
INSERT INTO
    levels (level)
VALUES
    ('good'),
    ('medium'),
    ('bad');
"""
#Pas clair sur comment compléter ces deux tables, est-ce que je dois les décortiquer en d'autres tables ?
create_requirements = """
INSERT INTO
    requirements (level, row, column, seat)
VALUES
    ();
"""

create_desks = """
INSERT INTO
    desks (row, column, seat)
VALUES
    ();
"""


execute_query(connection, create_students)
execute_query(connection, create_levels)
execute_query(connection, create_requirements)
execute_query(connection, create_desks)

#Sélectionner une valeur d'un tableau

#Fonction pour simplifier : This function accepts the connection object and the SELECT query and returns the selected record.
def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")


select_students = "SELECT * FROM students"
students = execute_read_query(connection, select_students)

for student in students:
    print(student)

#Sélectionner 1 valeur précise (FONCTIONNE PAS)
select_students = "SELECT student FROM students WHERE id = 2"
students = execute_read_query(connection, select_students)

for student in students:
    print(student)

#Changer une valeur
update_students = """
UPDATE 
    students
SET
    student = "Enzo"
WHERE
    id = 2
"""

execute_query(connection, update_students)

#Lier 2 tables ensemble

