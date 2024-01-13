from .math2 import *
def ceil(x):
    if x == int(x):
        return int(x)
    else:
        return int(x) + 1

def comb(n, k):
    if not isinstance(n, int) or not isinstance(k, int):
        raise TypeError("两个参数都应该为整数")
    if n < 0 or k < 0:
        raise ValueError("两个参数都应该为非负整数.")
    if 0 <= k <= n:
        return factorial(n) // (factorial(k) * factorial(n - k))
    else:
        return 0

def copysign(x, y):
    if y < 0:
        return -abs(x)
    else:
        return abs(x)

def fabs(x):
    if x < 0:
        return -x
    else:
        return x

def factorial(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("factorial() requires a positive integer")
    if n == 0:
        return 1
    return n * factorial(n - 1)

def floor(x):
    if x >= 0:
        return int(x)
    else:
        int_part = int(x)
        return int_part if x == int_part else int_part - 1

def frexp(x):
    if x == 0.0:
        return (0.0, 0)

    sign = 1 if x > 0 else -1
    x = abs(x)

    e = 0
    while x >= 1.0:
        x /= 2.0
        e += 1

    return (sign * x, e)

def fsum(iterable):
    partials = []
    for x in iterable:
        i = 0
        for y in partials:
            if abs(x) < abs(y):
                x, y = y, x
            hi = x + y
            lo = y - (hi - x)
            if lo:
                partials[i] = lo
                i += 1
            x = hi
        partials[i:] = [x]

    return sum(partials, 0.0)


def fmod(x, y):
    if y == 0.0:
        raise ValueError("fmod() division by zero")
    n = x / y
    n = int(n)
    result = x - n * y
    return result

def frexp(x):
    if x == 0.0:
        return (0.0, 0)

    sign = 1 if x > 0 else -1
    x = abs(x)

    exponent = int(log(x,2))
    mantissa = x / (2 ** exponent)

    return (sign * mantissa, exponent)

def gcd(*integers):
    if not integers:
        raise ValueError("gcd() requires at least one argument")

    result = integers[0]
    for num in integers[1:]:
        while num:
            result, num = num, result % num

    return abs(result)

def pow(a, n):
    if n == 0:
        return 1
    elif n % 2 == 1:
        return pow(a, n - 1) * a
    else:
        temp = pow(a, n // 2)
        return temp * temp

def exp(x):
    result = 1.0
    term = 1.0
    for i in range(1, 1000):
        term *= x / i
        result += term
    return result

