#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """
    Divides each element of my_list_1 by the corresponding element in my_list_2.
    Returns a new list containing the results for up to list_length elements.
    Handles different exceptions and prints appropriate messages when necessary.
    """
    result_list = []
    for i in range(list_length):
        try:
            # Attempt to retrieve elements and perform division
            num1 = my_list_1[i]
            num2 = my_list_2[i]
            result = num1 / num2
        except TypeError:
            print("wrong type")
            result = 0
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except IndexError:
            print("out of range")
            result = 0
        finally:
            result_list.append(result)
    return result_list
