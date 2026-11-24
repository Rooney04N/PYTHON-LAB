"""Experiment 7. Clean a student CSV and explore marks and attendance."""

import argparse
from pathlib import Path

import pandas as pd


DEFAULT_CSV = Path(__file__).resolve().parent / "data" / "exp07_students.csv"


def clean_students(students):
    required = {"Name", "Department", "Attendance", "Mark"}
    missing = required.difference(students.columns)
    if missing:
        raise ValueError("Missing CSV columns: " + ", ".join(sorted(missing)))

    # Count each observation once when calculating replacement values.
    cleaned = students.drop_duplicates().copy()
    for column in ("Attendance", "Mark"):
        values = pd.to_numeric(cleaned[column], errors="coerce")
        if values.count() == 0:
            raise ValueError(f"{column} needs at least one numeric value.")
        cleaned[column] = values.fillna(values.mean())

    for column in ("Name", "Department"):
        modes = cleaned[column].mode()
        replacement = modes.iloc[0] if not modes.empty else "Unknown"
        cleaned[column] = cleaned[column].fillna(replacement)

    return cleaned.drop_duplicates(ignore_index=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "csv", nargs="?", type=Path, default=DEFAULT_CSV,
        help="student CSV file (defaults to the six-student lab example)",
    )
    args = parser.parse_args()
    try:
        students = pd.read_csv(args.csv)
        cleaned = clean_students(students)
    except (OSError, ValueError) as error:
        parser.error(str(error))

    print("--- First five rows ---")
    print(students.head())
    print("\n--- Column information ---")
    students.info()
    print("\nMissing values before cleaning:")
    print(students.isna().sum())
    print("\n--- Cleaned dataset ---")
    print(cleaned.to_string(index=False))
    print("\n--- Descriptive statistics ---")
    print(cleaned[["Attendance", "Mark"]].describe().round(2))
    print("\n--- Department-wise average marks ---")
    print(cleaned.groupby("Department")["Mark"].mean().round(2))
    print("\n--- EDA summary ---")
    print(f"Highest mark: {cleaned['Mark'].max():.2f}")
    print(f"Lowest mark: {cleaned['Mark'].min():.2f}")
    print(f"Average mark: {cleaned['Mark'].mean():.2f}")
    print(f"Average attendance: {cleaned['Attendance'].mean():.2f}")


if __name__ == "__main__":
    main()
