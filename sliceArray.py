def take(arr,n):
    return arr[:n]

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def mod(a, b):
    return a % b

def exponent(a, b):
    return a ** b

def subt(a, b):
    return a - b



def remove_char(s):
    s = list(s)
    s.pop()
    s.pop(0)
    return ''.join(s)