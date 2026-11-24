# Python Lab · Cycle I

Seven Python 3 experiments from the Chennai Institute of Technology *Exploration in Artificial Intelligence* lab manual.

| No. | Experiment | Try it |
| --- | --- | --- |
| 1 | [Student marks, percentage, grade and academic performance](exp01_student_marks.py) | Enter Priya's marks of 85, 78, 92, 88 and 81. Her total is 424, her percentage is 84.80%, and her grade is A. |
| 2 | [Electricity billing with conditional statements and loops](exp02_electricity_billing.py) | Enter 350 units for Arun. The bill is Rs. 1,000.00 at the manual's slab rates. |
| 3 | [Menu-driven student information management](exp03_student_information.py) | Add a student, find the record by roll number, then delete it. |
| 4 | [Student records using lists, tuples, dictionaries, text and CSV](exp04_student_records.py) | Write three records to text and CSV, then read the CSV back. |
| 5 | [IoT sensor analysis using NumPy](exp05_sensor_analysis.py) | Identify the three readings above 28.0 and calculate the mean of all ten readings. |
| 6 | [Student marks using a Pandas Series and DataFrame](exp06_student_dataset.py) | Find the class average and list the students scoring above 85. |
| 7 | [Data cleaning and exploratory analysis using Pandas](exp07_student_eda.py) | Fill missing attendance and marks, remove duplicates and calculate department averages. |

## Run the programs

Open a terminal in the folder containing this README. To run an experiment, pass its filename to Python.

```sh
python exp01_student_marks.py
```

Experiments 1–4 use the Python standard library. Experiment 4 writes `students.txt` and `students.csv` in the current folder each time it runs.

For experiments 5–7, install the dependencies once, then run the file you want.

```sh
python -m pip install -r requirements.txt
python exp05_sensor_analysis.py
```

Experiment 7 loads the [six-student dataset](data/exp07_students.csv) by default. To run the [five-student Colab example](data/students1.csv), pass its filename.

```sh
python exp07_student_eda.py
python exp07_student_eda.py data/students1.csv
```
