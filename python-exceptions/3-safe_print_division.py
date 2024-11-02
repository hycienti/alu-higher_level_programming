#!/usr/bin/python3
def safe_print_division(a, b):
    """
    Divides two integers and prints the result in the finally block.
    Returns the result of the division, or None if an exception occurs.
    """
    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
