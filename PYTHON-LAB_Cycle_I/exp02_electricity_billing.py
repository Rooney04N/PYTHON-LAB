"""Experiment 2. Calculate a slab-based electricity bill for each customer."""

from math import isfinite


def calculate_bill(units):
    if not isfinite(units) or units < 0:
        raise ValueError("Units must be a finite, non-negative number.")
    if units <= 100:
        return units * 1.50
    if units <= 200:
        return 100 * 1.50 + (units - 100) * 2.50
    if units <= 500:
        return 100 * 1.50 + 100 * 2.50 + (units - 200) * 4.00
    return 100 * 1.50 + 100 * 2.50 + 300 * 4.00 + (units - 500) * 6.00


def main():
    customers = int(input("Enter number of customers: "))
    if customers < 1:
        raise ValueError("Enter at least one customer.")

    for number in range(1, customers + 1):
        print(f"\nCustomer {number}")
        name = input("Enter customer name: ").strip()
        units = float(input("Enter units consumed: "))
        bill = calculate_bill(units)
        print("Customer name:", name)
        print("Units:", units)
        print(f"Bill amount: Rs. {bill:.2f}")


if __name__ == "__main__":
    try:
        main()
    except ValueError as error:
        raise SystemExit(f"Input error: {error}")
