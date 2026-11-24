"""Experiment 1. Calculate a student's total, percentage and academic grade."""


def grade_and_performance(percentage):
    if percentage >= 90:
        return "A+", "Outstanding"
    if percentage >= 80:
        return "A", "Excellent"
    if percentage >= 70:
        return "B", "Very Good"
    if percentage >= 60:
        return "C", "Good"
    if percentage >= 50:
        return "D", "Average"
    return "F", "Needs Improvement"


def main():
    name = input("Enter student name: ").strip()
    subjects = int(input("Enter number of subjects: "))
    if subjects < 1:
        raise ValueError("Enter at least one subject.")

    total = 0.0
    for subject in range(1, subjects + 1):
        mark = float(input(f"Enter mark for subject {subject} (out of 100): "))
        if not 0 <= mark <= 100:
            raise ValueError("Each mark must be between 0 and 100.")
        total += mark

    # Each subject is marked out of 100, so the average mark is the percentage.
    percentage = total / subjects
    grade, performance = grade_and_performance(percentage)
    print("\n--- Academic performance ---")
    print("Student name:", name)
    print("Total marks:", total)
    print(f"Percentage: {percentage:.2f}%")
    print("Grade:", grade)
    print("Performance:", performance)


if __name__ == "__main__":
    try:
        main()
    except ValueError as error:
        raise SystemExit(f"Input error: {error}")
