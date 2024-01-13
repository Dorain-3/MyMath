from .math1 import factorial,exp

# 算圆周率
def leibniz_pi(num_terms):
    pi = 0.0
    sign = 1
    for i in range(num_terms):
        denominator = 2 * i + 1
        term = 4 / denominator * sign
        pi += term
        sign = -sign
    return pi



def floattopercent(a):
    try:
        if (a[-2:] == '.0'):
            return 0
        a = int(a)
        return 1  # 尝试将输入转换为整数
    except ValueError:
        decimal_places_num2 = len(a.split('.')[1]) if '.' in a else 0
        return decimal_places_num2


# a底数 b次数
def exponentiation(a, b):
    if ((a == 0 and b < 0) or (
            a < 0 and abs(int(float(b) * 10 ** floattopercent(str(b)))) % 2 == 1 and floattopercent(str(b)) > 0)):
        return 0
    else:
        result = 1
        if (b < 0):
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


# a为弧度制系数，π的系数
def sin(a):
    result = 0
    a = a * leibniz_pi(150)
    for i in range(1, 150, 2):
        result = result + ((exponentiation(a, float(i))) / factorial(i)) * ((-1) ** ((i + 1) / 2 - 1))
    return result


# a为弧度制系数，π的系数
def cos(a):
    result = 0
    a = a * leibniz_pi(150)
    for i in range(0, 150, 2):
        result = result + ((exponentiation(a, float(i))) / factorial(i)) * ((-1) ** (i / 2))
    return result


# a为弧度制系数，π的系数
def tan(a):
    return sin(a) / cos(a)


# a为弧度制系数，π的系数
def cot(a):
    return cos(a) / sin(a)


# 余割，a为弧度制系数，π的系数
def csc(a):
    return 1 / sin(a)


# 正割，a为弧度制系数，π的系数
def sec(a):
    return 1 / cos(a)


# asin，a为-1~1
def asin(a):
    result = 0
  
    for i in range(1, 150, 2):
        result = result + (float(factorial(((i - 1) / 2) * 2)) / (
                    exponentiation(float(4), float(((i - 1) / 2))) * (i) * (float(factorial(((i - 1) / 2))) ** 2))) * (a ** (i))
    return result


# acos，a为-1~1
def acos(a):
    result = 0
 
    for i in range(1, 150, 2):
        n = int((i - 1) / 2)
        result = result + (
                    float(factorial((i - 1))) / (exponentiation(float(4), float(n)) * i * ((factorial(n)) ** 2))) * (a ** (i))
    return leibniz_pi(150) / 2 - result


def atan(x):
    result=acos(nth_root(1/(1+x*x),2))
    if(x<0): 
        result=-result
    return result

def ln(a):
    if (a <= 0):
        print("输入无效")
        return 0
    else:
        result = 0
        for i in range(1, 150, 2):
            result = result + (((a - 1) / (a + 1)) ** i) * (1 / i)
        return result * 2

# a为底数，b为对数
def log(a, b):
    if (a <= 0 or b <= 0):
        print("输入无效")
        return 0
    elif (a==1):
        return 0
    else:
        return ln(b) / ln(a)
    
def sinh(a):
    return (exp(a)-exp(-a))/2

def tanh(a):
    result=0
    for i in range(1,100):
        result=result+factorial(i)/(2**i-1)*(a**(2*i-1))
    return result

def cosh(a):
    return (exp(a)+exp(-a))/2

def asinh(a):
    return ln(a+exponentiation(a**2+1,0.5))

def acosh(a):
    return ln(a+exponentiation(a**2-1,0.5))

def atanh(a):
    return 0.5*ln((a+1)/(a-1))