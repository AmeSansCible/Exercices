import random
import tkinter as tk

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

    def generate_random_seating(self, students):
        shuffled_students = random.sample(students, len(students))
        index = 0
        for row in range(0, self.rows, 2):
            for column in range(self.columns):
                if index < len(shuffled_students):
                    self.assign_seat(row, column, shuffled_students[index])
                    index += 1
            for column in range(self.columns):
                if index < len(shuffled_students):
                    self.assign_seat(row+1, column, shuffled_students[index])
                    index += 1
                else:
                    return

class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

def display_seating_arrangement(classroom):
    root = tk.Tk()
    root.title("Seating Arrangement")

    for row_index, row in enumerate(classroom.seats):
        for col_index, student in enumerate(row):
            if student:
                label_text = f"{student.first_name} {student.last_name}"
            else:
                label_text = "Empty"
            label = tk.Label(root, text=label_text, relief="solid", width=20, height=2)
            label.grid(row=row_index, column=col_index)

    root.mainloop()

if __name__ == "__main__":
    # Créer une salle de classe avec 5 rangées et 4 colonnes
    classroom = Classroom(5, 6)

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
    classroom.generate_random_seating(students)

    # Afficher l'arrangement des sièges
    display_seating_arrangement(classroom)
