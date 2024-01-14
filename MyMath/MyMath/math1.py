def ceil(x):
    if not isinstance(x, int) and not isinstance(x, float):
        raise ValueError("参数应为任意实数.")
    if x == int(x):
        return int(x)
    else:
        return int(x) + 1


def comb(n, k):
    if n < 0 or k < 0 or not isinstance(n, int) or not isinstance(k, int):
        raise ValueError("两个参数都应该为非负整数.")
    if 0 <= k <= n:
        return factorial(n) // (factorial(k) * factorial(n - k))
    else:
        return 0


def copysign(x, y):
    a = 1.0 if y >= 0.0 else -1.0
    if str(y) == str(-0.0):
        a = -1.0
    return abs(x) * a


def fabs(x):
    if x < 0:
        return -x
    else:
        return x


def factorial(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("factorial() 需要正整数")
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
        return 0.0, 0

    sign = 1 if x > 0 else -1
    x = abs(x)

    e = 0
    while x >= 1.0:
        x /= 2.0
        e += 1

    return sign * x, e


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
        raise ValueError("fmod() 除数为0")
    n = x / y
    n = int(n)
    result = x - n * y
    return result


def gcd(*integers):
    if not integers:
        raise ValueError("gcd() 至少需要一个参数")

    result = integers[0]
    for num in integers[1:]:
        while num:
            result, num = num, result % num

    return abs(result)


def isfinite(x):
    return not (isnan(x) or isinf(x))


def isinf(x):
    return x == float('inf') or x == float('-inf')


def isnan(x):
    return x != x


def isqrt(x):
    from .math2 import nth_root
    return int(nth_root(x, 2))


def lcm(*integers):
    if not integers:
        return 1

    result = integers[0]
    for i in integers:
        if i == 0:
            return 0
        result = result * i // gcd(result, i)

    return result


def ldexp(m, e):
    return m * (2 ** e)


def modf(x):
    if not isinstance(x, (int, float)):
        raise TypeError("modf()输入必须为整型或浮点数")

    integer_part = int(x)
    decimal_part = x - integer_part

    return decimal_part, integer_part


def turnc(x):
    return int(x)


def pow(a, n, z):
    fa = float(a)
    fn = float(n)
    if (n == 0):
        return 1
    elif (n % 2 == 1):
        return pow(a, n - 1) * a % z
    else:
        result = pow(a, n / 2) % z
        return result * result % z


def exp(x):
    result = 1.0
    term = 1.0
    for i in range(1, 1000000):
        term *= x / i
        result += term
    return result
