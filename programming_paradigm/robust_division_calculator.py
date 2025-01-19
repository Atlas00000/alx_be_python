# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """
    Safely performs division and handles errors like division by zero
    and non-numeric inputs.

    Parameters:
        numerator (str): The numerator as a string (to handle non-numeric input).
        denominator (str): The denominator as a string (to handle non-numeric input).

    Returns:
        str: The result of the division or an error message.
    """
    try:
        # Attempt to convert inputs to floats
        numerator = float(numerator)
        denominator = float(denominator)

        # Perform division
        result = numerator / denominator
        return f"The result of the division is {result}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."
