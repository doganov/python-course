# -*- coding: utf-8 -*-

# Модул за числата на Фибоначи

PI = 3.14

def fib(n): # Извежда числата на Фибоначи до n
    a, b = 0, 1
    while b < n:
        print b,
        a, b = b, a + b

def fib2(n): # Връща числата на Фибоначи до n
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a + b
    return result

if __name__ == "__main__":
    print "IMPORTED!"
    a = 100
    import sys
    fib(int(sys.argv[1]))
