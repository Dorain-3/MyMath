# 计算阶乘
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


# 计算余弦值
def shushu_cosine(degrees, terms=10):
    radians = degrees * (3.141592653589793 / 180)  # 角度转弧度
    result = 0
    for n in range(terms):
        term = ((-1) ** n) * (radians ** (2 * n)) / factorial(2 * n)
        result += term
    return result


def shushu_sine(degrees, terms=10):
    radians = degrees * (3.141592653589793 / 180)
    result = 0
    for n in range(terms):
        term = ((-1) ** n) * (radians ** (2 * n + 1)) / factorial(2 * n + 1)
        result += term
    return result


print(shushu_cosine(60))
