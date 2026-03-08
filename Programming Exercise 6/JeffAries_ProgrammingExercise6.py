"""Validation Program

Validates phone numbers, Social Security numbers, and zipcodes using
regular expressions.
"""

import re


def validate_phone_number(phone_number: str) -> bool:
    """Validate phone number.

    Parameters:
        phone_number (str): The phone number entered by the user."""

    # Store the regular expression for valid phone number formats.
    pattern = r"^(?:\(\d{3}\)\s?\d{3}-\d{4}|\d{3}-\d{3}-\d{4})$"

    # Return True when the full string matches the pattern.
    return bool(re.fullmatch(pattern, phone_number))


def validate_ssn(ssn: str) -> bool:
    """Validate a Social Security number.

    Parameters:
        ssn (str): The Social Security number entered by the user."""

    # Store the regular expression for a standard SSN.
    pattern = r"^\d{3}-\d{2}-\d{4}$"

    # Return True when the full string matches the pattern.
    return bool(re.fullmatch(pattern, ssn))


def validate_zip_code(zip_code: str) -> bool:
    """Validate a U.S. ZIP code.

    Parameters:
        zip_code (str): The ZIP code entered by the user."""

    # Store the regular expression for valid ZIP code formats.
    pattern = r"^\d{5}(?:-\d{4})?$"

    # Return True when the full string matches the pattern.
    return bool(re.fullmatch(pattern, zip_code))


def display_validation_result(label: str, value: str, is_valid: bool) -> None:
    """Display whether one entered value is valid.

    Parameters:
        label (str): The type of value being checked.
        value (str): The value entered or tested.
        is_valid (bool): The result of the validation check."""

    # Choose the display text based on the validation result.
    status = "Valid" if is_valid else "Invalid"

    # Display the validation result in a readable sentence.
    print(f"{label}: {value} -> {status}")


def run_tests() -> None:
    """Run sample tests for all validation functions."""

    # Create sample phone number test cases.
    phone_tests = [
        "941-555-1234",
        "(941) 555-1234",
        "9415551234",
        "94-555-1234",
    ]

    # Create sample SSN test cases.
    ssn_tests = [
        "123-45-6789",
        "000-12-3456",
        "123456789",
        "12-345-6789",
    ]

    # Create sample ZIP code test cases.
    zip_tests = [
        "34205",
        "34205-1234",
        "3420",
        "34205-123",
    ]

    # Display the phone number test section.
    print("\nPhone Number Test Cases")
    print("-" * 40)

    # Test each sample phone number.
    for item in phone_tests:
        display_validation_result("Phone number", item, validate_phone_number(item))

    # Display the Social Security number test section.
    print("\nSocial Security Number Test Cases")
    print("-" * 40)

    # Test each sample Social Security number.
    for item in ssn_tests:
        display_validation_result("SSN", item, validate_ssn(item))

    # Display the ZIP code test section.
    print("\nZIP Code Test Cases")
    print("-" * 40)

    # Test each sample ZIP code.
    for item in zip_tests:
        display_validation_result("ZIP code", item, validate_zip_code(item))


def main() -> None:
    """Run the validation program."""

    # Display the title of the program.
    print("Regular Expression Validation Program")
    print("=" * 40)

    # Run built-in tests before asking the user for input.
    run_tests()

    # Ask the user to enter a phone number.
    phone_number = input(
        "\nEnter a phone number (###-###-#### or (###) ###-####): "
    ).strip()

    # Ask the user to enter a Social Security number.
    ssn = input("Enter a Social Security number (###-##-####): ").strip()

    # Ask the user to enter a ZIP code.
    zip_code = input("Enter a ZIP code (##### or #####-####): ").strip()

    # Display the user's validation results.
    print("\nUser Input Results")
    print("-" * 40)
    display_validation_result(
        "Phone number",
        phone_number,
        validate_phone_number(phone_number),
    )
    display_validation_result("SSN", ssn, validate_ssn(ssn))
    display_validation_result("ZIP code", zip_code, validate_zip_code(zip_code))


if __name__ == "__main__":
    # Call the main function when the file is executed directly.
    main()