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
    ('good', 'A', '1', 'left'),
    ('medium', 'B', '2', 'right'),
    ('bad', 'C', '3', 'middle');
"""

create_desks = """
INSERT INTO
    desks (row, column, seat)
VALUES
    (1, 1, 1),
    (1, 2, 1),
    (2, 1, 1);
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

#Sélectionner 1 valeur précise
select_students = "SELECT first_name, name FROM students WHERE id = 2"
students = execute_read_query(connection, select_students)

for student in students:
    print(student)

#Changer une valeur
update_students = """
UPDATE 
    students
SET
    first_name = "Enzo"
WHERE
    id = 2
"""

execute_query(connection, update_students)

#Lier 2 tables ensemble (relationnel) : table intermédiaire qui associe les élèves (students) aux niveaux (levels)
#Les FOREIGN KEY permettent de relier les identifiants des étudiants (students.id) et des niveaux (levels.id).
#Ajout d'une contrainte d’unicité (PRIMARY KEY) pour éviter les doublons
create_student_levels_table = """
CREATE TABLE student_levels (
    student_id INTEGER UNIQUE,
    level_id INTEGER,
    PRIMARY KEY (student_id, level_id),
    FOREIGN KEY (student_id) REFERENCES students (id),
    FOREIGN KEY (level_id) REFERENCES levels (id)
);
"""
execute_query(connection, create_student_levels_table)

#Ajouter des données
create_student_levels = """
    INSERT INTO 
        student_levels (student_id, level_id)
    VALUES
        (1, 1), -- Maeva a un bon niveau
        (2, 2), -- Noémie a un niveau moyen
        (3, 3); -- Nathan a un mauvais niveau
"""
execute_query(connection, create_student_levels)

#Requête pour obtenir les étudiants avec leur level. Relie les données des étudiants (students) aux niveaux (levels) en passant par la table relationnelle student_levels

select_students_with_levels = """
SELECT 
    students.first_name, students.name, levels.level -- récupère les colonnes first_name, name et level des tables students et levels
FROM -- spécifie la table sur laquelle on travaille. Students est notre point de départ pour la jointure
    students 
INNER JOIN -- Associe chaque étudiant de students à son enregistrement dans student_levels.
    student_levels ON students.id = student_levels.student_id
INNER JOIN -- Associe chaque enregistrement de student_levels au niveau correspondant dans levels
    levels ON student_levels.level_id = levels.id;
"""
# Si je rajoute la ligne de code WHERE levels.level = 'good'; cela me permettrait de récupérer les étudiants d'un level spécifique


students_with_levels = execute_read_query(connection, select_students_with_levels)

for student in students_with_levels:
    print(student)


