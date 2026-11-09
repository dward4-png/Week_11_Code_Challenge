# CIS 105 - Code Challenge: Grade Book
# Name: Dylan Ward
# Section: CIS 105-01
#
# Complete the five functions below where you see # TODO.
# Do not change the test code at the bottom of the file.
#
# The grade book is a dictionary:
#   keys   = student names (strings)
#   values = lists of test scores (numbers)
# Example: {"Alex": [90, 85, 95], "Jordan": [70, 80]}


def add_student(book, name):
    """Add a new student with an empty score list."""

    if name in book:
        print("Student already exists.")
    else:
        book[name] = []


def add_grade(book, name, grade):
    """Add a score to a student's list."""

    if name not in book:
        add_student(book, name)

    book[name].append(grade)


def student_average(book, name):
    """Return the average of a student's scores."""

    grades = book.get(name)

    if grades is None:
        return None

    if len(grades) == 0:
        return 0

    return sum(grades) / len(grades)


def top_student(book):
    """Return the name of the student with the highest average."""

    best_student = None
    highest_average = -1

    for name in book:
        average = student_average(book, name)

        if average is not None and average > highest_average:
            highest_average = average
            best_student = name

    return best_student


def print_report(book):
    """Print every student, scores, and average."""

    for name, grades in book.items():
        average = student_average(book, name)
        print(name, grades, "Average:", average)


# ---------------- TEST CODE - DO NOT CHANGE BELOW THIS LINE ----------------

gradebook = {}

add_student(gradebook, "Alex")
add_student(gradebook, "Jordan")
add_student(gradebook, "Taylor")

add_grade(gradebook, "Alex", 90)
add_grade(gradebook, "Alex", 85)
add_grade(gradebook, "Alex", 95)

add_grade(gradebook, "Jordan", 70)
add_grade(gradebook, "Jordan", 80)

add_grade(gradebook, "Taylor", 100)
add_grade(gradebook, "Taylor", 95)
add_grade(gradebook, "Taylor", 90)
add_grade(gradebook, "Taylor", 85)

print_report(gradebook)
print("Top student:", top_student(gradebook))

# Expected output:
# Alex: [90, 85, 95] Average: 90.0
# Jordan: [70, 80] Average: 75.0
# Taylor: [100, 95, 90, 85] Average: 92.5
# Top student: Taylor
