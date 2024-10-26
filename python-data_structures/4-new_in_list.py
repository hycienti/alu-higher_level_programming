#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    # Create a copy of the original list
    new_list = my_list[:]
    
    # Check if idx is within the valid range
    if 0 <= idx < len(new_list):
        new_list[idx] = element
    
    # Return the modified copy (or the original copy if index is invalid)
    return new_list
