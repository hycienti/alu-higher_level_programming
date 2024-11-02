#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0  # Keep track of the actual number of integers printed
    
    for i in range(x):
        try:
            # Attempt to format and print the item as an integer
            print("{:d}".format(my_list[i]), end="")
            count += 1  # Increment count only if the item is an integer
        except (ValueError, TypeError):
            # If the item is not an integer, skip it silently
            continue
    
    print()  # Print a newline after all integers
    return count  # Return the number of integers printed
