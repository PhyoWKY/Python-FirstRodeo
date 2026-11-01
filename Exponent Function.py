print(2**3)

def raise_to_power(base, exponent):
    result = 1
    for index in range(exponent):
        result = result * base
    return result
print(raise_to_power(5, 3))