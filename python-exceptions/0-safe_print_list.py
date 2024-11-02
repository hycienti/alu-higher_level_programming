#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0  # Keep track of the actual number of elements printed
    try:
        for i in range(x):
            print(my_list[i], end="")  # Print element without a newline
            count += 1  # Increment the count for each printed element
    except IndexError:
        # This block will run if `x` is greater than the length of `my_list`
        pass  # Do nothing, just skip out of the loop
    print()  # Print a newline after all elements
    return count  # Return the actual number of elements printed
