# Dado un array del estilo: [0, 0, 1, 0], devolver el número en decimal => 2

def binary_array_to_number(arr):

    decimal = 0
    for digit in arr:
        decimal = decimal*2 + int(digit)

    return decimal

print(binary_array_to_number([0, 1, 1, 0]))



# Soluciones más simples

def binary_array_to_number(arr):
    return int("".join(map(str, arr)), 2)



def binary_array_to_number(arr):
    return int(''.join(str(a) for a in arr), 2)



def binary_array_to_number(arr):
    return sum(digit * 2**i for i, digit in enumerate(reversed(arr)))