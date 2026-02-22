"""Monthly Expenses Program

Collects user's monthly expenses & use
functools.reduce() to calculate:
  - Total monthly expenses
  - Highest expense
  - Lowest expense
"""

from __future__ import annotations

from functools import reduce


def get_positive_float(prompt: str) -> float:
    """Get a positive number from the user.

    Parameters:
        prompt (str): Message shown to the user.

    Variables:
        raw (str): User input.
        value (float): Converted number.

    Steps:
        1. Ask the user for input.
        2. Try to convert it to a float.
        3. Make sure it is 0 or greater.
        4. Keep asking until valid.

    Return:
        float: A valid non-negative number.
    """
    while True:
        # Ask the user for a number.
        raw = input(prompt).strip()

        try:
            # Convert the input to a float.
            value = float(raw)

            # Ensure the number is not negative.
            if value < 0:
                print("Please enter a value of 0 or greater.")
                continue

            return value

        except ValueError:
            # Handle non-numeric input.
            print("Please enter a valid number (example: 125.50).")


def get_expenses() -> list[tuple[str, float]]:
    """Collect expense entries from the user.

Parameters:
    None

Variables:
    expenses (list): Stores (expense type, amount).
    expense_type (str): Name of the expense.
    amount (float): Cost of the expense.

Steps:
    1. Tell the user how to enter expenses and how to stop.
    2. Ask for the expense type.
    3. If blank, stop (after at least one entry).
    4. Ask for the amount and validate it.
    5. Add the (type, amount) to the list.

Return:
    list: A list of (type, amount) pairs.
    """
    expenses: list[tuple[str, float]] = []

    print("Enter your monthly expenses. Press Enter on the expense type to finish.")

    while True:
        # Ask for the expense label.
        expense_type = input("Expense type (example: Rent): ").strip()

        # Blank input ends the list.
        if expense_type == "":
            if expenses:
                break

            print("You must enter at least one expense.")
            continue

        # Ask for the expense amount.
        amount = get_positive_float(f"Amount for {expense_type}: $")

        # Save the entry.
        expenses.append((expense_type, amount))

        print()  # Blank line for readability.

    return expenses


def analyze_expenses(expenses: list[tuple[str, float]]) -> dict[str, object]:
    """Analyze expenses using reduce.

Parameters:
    expenses (list): List of (type, amount) pairs.

Variables:
    total (float): Total of all amounts.
    highest (tuple): Expense with the largest amount.
    lowest (tuple): Expense with the smallest amount.

Steps:
    1. Use reduce to calculate the total.
    2. Use reduce to find the highest expense.
    3. Use reduce to find the lowest expense.
    4. Return the results in a dictionary.

Return:
    dict: Contains 'total', 'highest', and 'lowest'.
    """
    # Use reduce to calculate the total.
    total = reduce(lambda acc, item: acc + item[1], expenses, 0.0)

    # Use reduce to find the highest (max) expense entry.
    highest = reduce(lambda best, item: item if item[1] > best[1] else best, expenses)

    # Use reduce to find the lowest (min) expense entry.
    lowest = reduce(lambda best, item: item if item[1] < best[1] else best, expenses)

    return {"total": total, "highest": highest, "lowest": lowest}


def display_report(results: dict[str, object]) -> None:
    """Display the expense report.

Parameters:
    results (dict): Dictionary with total, highest, and lowest.

Variables:
    total (float): Total expenses.
    highest (tuple): Highest expense (type, amount).
    lowest (tuple): Lowest expense (type, amount).

Steps:
    1. Get total, highest, and lowest from the dictionary.
    2. Print the results with labels and money formatting.

Return:
    None
    """
    total = float(results["total"])
    highest = results["highest"]
    lowest = results["lowest"]

    print("\n--- Monthly Expense Summary ---")
    print(f"Total monthly expenses: ${total:,.2f}")
    print(f"Highest expense: {highest[0]} (${highest[1]:,.2f})")
    print(f"Lowest expense:  {lowest[0]} (${lowest[1]:,.2f})")


def main() -> None:
    """Run the monthly expenses program.

    Parameters:
        None

    Variables:
        expenses (list[tuple[str, float]]): The user's entered expenses.
        results (dict[str, object]): The analysis results.

    Logical steps:
        1. Collect expenses from the user.
        2. Analyze the list using reduce.
        3. Display the report.

    Return:
        None
    """
    expenses = get_expenses()

    results = analyze_expenses(expenses)

    display_report(results)


if __name__ == "__main__":
    main()