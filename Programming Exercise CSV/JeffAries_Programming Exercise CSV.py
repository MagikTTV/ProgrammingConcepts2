"""
Grades CSV Program

This program allows an instructor to:
1. Enter student names and three exam grades.
2. Store the data in a CSV file named grades.csv.
3. Read the CSV file and display the data in table format.
"""

import csv


def create_grades_file():
    """
    Create a CSV file with student grade data.

    Parameters:
        None

    Variables:
        num_students (int): Number of students to enter.
        first_name (str): Student's first name.
        last_name (str): Student's last name.
        exam1 (int): Exam 1 grade.
        exam2 (int): Exam 2 grade.
        exam3 (int): Exam 3 grade.
        file (file object): CSV file handler.

    Return:
        None
    """

    # Ask user for number of students
    num_students = int(input("Enter number of students: "))

    # Open CSV file for writing
    with open("grades.csv", "w", newline="") as file:
        writer = csv.writer(file)

        # Write header
        writer.writerow(["First Name", "Last Name", "Exam 1", "Exam 2", "Exam 3"])

        # Loop through students
        for i in range(num_students):
            print(f"\nEntering data for student #{i + 1}")

            # Get student information
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")

            exam1 = int(input("Enter Exam 1 grade: "))
            exam2 = int(input("Enter Exam 2 grade: "))
            exam3 = int(input("Enter Exam 3 grade: "))

            # Write row to CSV
            writer.writerow([first_name, last_name, exam1, exam2, exam3])

    print("\nGrades successfully written to grades.csv\n")


def display_grades_file():
    """
    Read and display the CSV file in tabular format.

    Parameters:
        None

    Variables:
        file (file object): CSV file handler.
        reader (csv.reader): CSV reader object.
        row (list): Each row from the CSV file.
    Return:
        None
    """

    print("\nStudent Grades:\n")

    # Open CSV file for reading
    with open("grades.csv", "r") as file:
        reader = csv.reader(file)

        # Print each row in formatted columns
        for row in reader:
            print("{:<15} {:<15} {:<10} {:<10} {:<10}".format(*row))


def main():
    """
    Main function to run the program.
    Return:
        None
    """

    create_grades_file()
    display_grades_file()


# Run the program
if __name__ == "__main__":
    main()