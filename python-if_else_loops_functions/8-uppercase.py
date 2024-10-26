#!/usr/bin/python3
def uppercase(str):
    result = ""
    for c in str:
        # Check if c is lowercase by ASCII value and convert to uppercase if so
        if ord('a') <= ord(c) <= ord('z'):
            result += "{:c}".format(ord(c) - 32)
        else:
            result += c
    print("{}".format(result))
