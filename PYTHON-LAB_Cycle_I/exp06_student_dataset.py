"""Experiment 6. Analyse student marks using a Pandas Series and DataFrame."""

import pandas as pd


def main():
    marks = [85, 91, 78, 88, 95]
    series = pd.Series(marks, index=["A", "B", "C", "D", "E"])
    print("--- Pandas Series ---")
    print(series)

    students = pd.DataFrame({
        "RollNo": [101, 102, 103, 104, 105],
        "Name": ["Anitha", "Bala", "Chitra", "Dinesh", "Ezhil"],
        "Department": ["CSE", "CSE", "ECE", "CSE", "ECE"],
        "Mark": marks,
    })
    print("\n--- DataFrame ---")
    print(students)
    print("\nAverage mark:", round(students["Mark"].mean(), 2))
    print("\nStudents scoring above 85:")
    print(students[students["Mark"] > 85])


if __name__ == "__main__":
    main()
