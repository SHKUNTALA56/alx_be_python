import sys
from robust_division_calculator import safe_divide

def main():
    """
    Main function to handle command-line arguments and perform safe division.
    """
    # Check for exactly two additional arguments
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
        sys.exit(1)

    # Extract command-line arguments
    numerator = sys.argv[1]
    denominator = sys.argv[2]

    # Perform safe division and print the result
    result = safe_divide(numerator, denominator)
    print(result)

if __name__ == "__main__":
    main()
