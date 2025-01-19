def safe_divide(numerator, denominator):
    """
    Safely divides two numbers, handling errors like division by zero and non-numeric inputs.
    :param numerator: The numerator for the division
    :param denominator: The denominator for the division
    :return: A string with the result of the division or an appropriate error message
    """
    try:
        # Convert inputs to floats
        num = float(numerator)
        denom = float(denominator)

        # Check for division by zero
        if denom == 0:
            return "Error: Cannot divide by zero."
        
        # Perform division and return the result
        return f"The result of the division is {num / denom:.2f}"
    
    # Catch the ValueError if the inputs are not valid numbers
    except ValueError:
        return "Error: Please enter numeric values only."
