"""Experiment 5. Summarise IoT sensor readings using NumPy."""

import numpy as np


def main():
    readings = np.array([24.5, 25.1, 26.3, 27.0, 28.2, 29.1, 27.8, 26.5, 25.7, 30.2])
    threshold = 28.0

    print("Sensor data:", readings)
    print(f"Mean: {np.mean(readings):.2f}")
    print(f"Median: {np.median(readings):.2f}")
    print("Minimum:", np.min(readings))
    print("Maximum:", np.max(readings))
    print(f"Population standard deviation: {np.std(readings):.2f}")
    print(f"Values above {threshold}:", readings[readings > threshold])


if __name__ == "__main__":
    main()
