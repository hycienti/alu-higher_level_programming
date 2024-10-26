#!/usr/bin/python3
def pow(a, b):
    result = 1
    if b < 0:
        a = 1 / a
        b = -b
    for _ in range(b):
        result *= a
    return round(result, 10)  # Rounding to avoid precision errors
