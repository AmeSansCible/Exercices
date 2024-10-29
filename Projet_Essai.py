import random


class Classroom:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.seats = [[None for _ in range(columns)] for _ in range(rows)]

    def assign_seat(self, row, column, student):
        if row < self.rows and column < self.columns:
            self.seats[row][column] = student
        else:
            print("Invalid seat position.")

    def print_seating_arrangement(self):
        for row in self.seats:
            print([student.first_name + " " + student.last_name if student else "Empty" for student in row])


class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


def generate_random_seating(classroom, students):
    shuffled_students = random.sample(students, len(students))
    index = 0
    for row in range(classroom.rows):
        for column in range(classroom.columns):
            if index < len(shuffled_students):
                classroom.assign_seat(row, column, shuffled_students[index])
                index += 1
            else:
                return


if __name__ == "__main__":
    # Créer une salle de classe avec 5 rangées et 4 colonnes
    classroom = Classroom(4, 6)

    # Liste des élèves
    students = [
        Student("Jean", "Dupont"),
        Student("Marie", "Dubois"),
        Student("Pierre", "Martin"),
        Student("Sophie", "Lefevre"),
        Student("Luc", "Moreau"),
        Student("Emma", "Garcia"),
        Student("Thomas", "Roux"),
        Student("Lea", "Andre"),
        Student("Louis", "Blanc"),
        Student("Camille", "Rousseau"),
        Student("Julie", "Vincent"),
        Student("Antoine", "Leroy")
    ]

    # Générer les places aléatoires
    generate_random_seating(classroom, students)

    # Afficher l'arrangement des sièges
    classroom.print_seating_arrangement()
