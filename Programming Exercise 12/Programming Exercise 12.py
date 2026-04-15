"""
Program Description:
This program reads student grade data from a CSV file and uses NumPy to perform analysis.
"""

# Import required modules
import numpy as np
import csv


def load_grades(filename):
    """
    Load grades from a CSV file into a NumPy array.

    Parameters:
        filename (str): Name of the CSV file

    Returns:
        numpy.ndarray: 2D array of exam grades (integers)
    """

    # Create an empty list to store grade data
    grades_list = []

    # Open the CSV file using with statement
    with open(filename, 'r') as file:
        reader = csv.reader(file)

        # Skip header row
        next(reader)

        # Loop through each row in the file
        for row in reader:
            # Extract exam scores (columns 2, 3, 4)
            exams = list(map(int, row[2:5]))
            grades_list.append(exams)

    # Convert list to NumPy array
    grades_array = np.array(grades_list)

    return grades_array


def print_exam_statistics(grades):
    """
    Calculate and print statistics for each exam.

    Parameters:
        grades (numpy.ndarray): 2D array of exam grades
    """

    # Loop through each column (exam)
    for i in range(grades.shape[1]):
        exam = grades[:, i]

        print(f"\nExam {i + 1} Statistics:")

        # Calculate statistics
        print(f"Mean: {np.mean(exam):.2f}")
        print(f"Median: {np.median(exam):.2f}")
        print(f"Standard Deviation: {np.std(exam):.2f}")
        print(f"Minimum: {np.min(exam)}")
        print(f"Maximum: {np.max(exam)}")


def print_overall_statistics(grades):
    """
    Calculate and print overall statistics across all exams.

    Parameters:
        grades (numpy.ndarray): 2D array of exam grades
    """

    # Flatten array to combine all exams
    all_grades = grades.flatten()

    print("\nOverall Statistics:")

    # Calculate statistics
    print(f"Mean: {np.mean(all_grades):.2f}")
    print(f"Median: {np.median(all_grades):.2f}")
    print(f"Standard Deviation: {np.std(all_grades):.2f}")
    print(f"Minimum: {np.min(all_grades)}")
    print(f"Maximum: {np.max(all_grades)}")


def analyze_pass_fail(grades):
    """
    Determine pass/fail counts and overall pass percentage.

    Parameters:
        grades (numpy.ndarray): 2D array of exam grades
    """

    total_pass = 0
    total_count = grades.size

    # Loop through each exam
    for i in range(grades.shape[1]):
        exam = grades[:, i]

        # Count passing and failing students
        passed = np.sum(exam >= 60)
        failed = np.sum(exam < 60)

        print(f"\nExam {i + 1} Pass/Fail:")
        print(f"Passed: {passed}")
        print(f"Failed: {failed}")

        total_pass += passed

    # Calculate overall pass percentage
    pass_percentage = (total_pass / total_count) * 100

    print(f"\nOverall Pass Percentage: {pass_percentage:.2f}%")


def print_sample_data(grades):
    """
    Print the first few rows of the dataset.

    Parameters:
        grades (numpy.ndarray): 2D array of exam grades
    """

    print("\nFirst Few Rows of Data:")
    print(grades[:5])


# Main function to run program
def main():
    """
    Main function to execute the program steps.
    """

    filename = "grades.csv"

    # Load data
    grades = load_grades(filename)

    # Display sample data
    print_sample_data(grades)

    # Print statistics per exam
    print_exam_statistics(grades)

    # Print overall statistics
    print_overall_statistics(grades)

    # Analyze pass/fail
    analyze_pass_fail(grades)


# Run the program
if __name__ == "__main__":
    main()