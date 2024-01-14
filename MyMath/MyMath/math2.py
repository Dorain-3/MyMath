from .math1 import *
from .mathematical_constants import *


def floattopercent(a):
    try:
        if a[-2:] == '.0':
            return 0
        a = int(a)
        return 1  # 尝试将输入转换为整数
    except ValueError:
        decimal_places_num2 = len(a.split('.')[1]) if '.' in a else 0
        return decimal_places_num2


# a底数 b次数
def exponentiation(a, b):
    if ((a == 0 and b < 0) or (
            a < 0 < floattopercent(str(b)) and abs(int(float(b) * 10 ** floattopercent(str(b)))) % 2 == 1)):
        return 0
    else:
        result = 1
        if b < 0:
            a = 1 / a
        for i in range(0, abs(int(float(b) * 10 ** floattopercent(str(b))))):
            result = result * a
        return nth_root(result, 10 ** floattopercent(str(b)))


# 开根号number数，n开几次，precision精度
def nth_root(number, n, precision=0.0000001):
    guess = number / 2.0
    while abs(guess ** n - number) > precision:
        guess = guess - (guess ** n - number) / (n * (guess ** (n - 1)))
    return guess


# a为弧度制
def sin(a):
    a %= 2*PI
    if(a > PI):
        return -sin(a-PI)
    elif (a > PI/2) :
        return  sin(PI-a)  
    result = 0
    for i in range(1, 150, 2):
        result = result + ((exponentiation(a, float(i))) / factorial(i)) * ((-1) ** ((i + 1) / 2 - 1))
    return result


# a为弧度制
def cos(a):
    return sin(PI/2-a)


# a为弧度制
def tan(a):
    return sin(a) / cos(a)


# a为弧度制
def cot(a):
    if(a==0):
        return "为中断点"
    return cos(a) / sin(a)


# 余割，a为弧度制
def csc(a):
    return 1 / sin(a)


# 正割，a为弧度制
def sec(a):
    return 1 / cos(a)


# asin，a为-1~1
def asin(a):
    result = 0

    for i in range(1, 150, 2):
        result = result + (float(factorial(((i - 1) / 2) * 2)) / (
                exponentiation(float(4), float(((i - 1) / 2))) * i * (float(factorial(((i - 1) / 2))) ** 2))) * (
                         a ** i)
    return result


# acos，a为-1~1
def acos(a):
    result = 0

    for i in range(1, 150, 2):
        n = int((i - 1) / 2)
        result = result + (
                float(factorial((i - 1))) / (exponentiation(float(4), float(n)) * i * ((factorial(n)) ** 2))) * (
                         a ** i)
    return PI / 2 - result


def atan(a):
    x=acos(sqrt(1/(1+a*a)))
    if(a>=0):
        return x
    else:
        return -x

def ln(a):
    if a <= 0:
        print("输入无效")
        return 0
    else:
        result = 0
        for i in range(1, 2000, 2):
            result = result + (((a - 1) / (a + 1)) ** i) * (1 / i)
        return result * 2


# a为底数，b为对数
def log(a, b):
    if a <= 0 or b <= 0:
        print("输入无效")
        return 0
    elif a == 1:
        return 0
    else:
        return ln(b) / ln(a)


def sinh(a):
    return (exp(a) - exp(-a)) / 2


def tanh(a):
    result = 0
    for i in range(1, 100):
        result = result + factorial(i) / (2 ** i - 1) * (a ** (2 * i - 1))
    return result


def cosh(a):
    return (exp(a) + exp(-a)) / 2


def asinh(a):
    return ln(a + exponentiation(a ** 2 + 1, 0.5))


def acosh(a):
    return ln(a + exponentiation(a ** 2 - 1, 0.5))


def atanh(a):
    return 0.5 * ln((a + 1) / (a - 1))
