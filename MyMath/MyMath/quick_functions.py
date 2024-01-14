"""
@author: Dorain-3
@email: 3174950356@qq.com
"""
from mathematical_constants import *
from math1 import *
from math2 import *


def quick_sin_angle(x):  # 快速正弦函数，输入角度
    if isinstance(x, str):
        x = float(x)
    signal = 0
    if x > 0.0:
        while x >= 360.0:
            x -= 360.0
    else:
        while x < 0.0:
            x += 360.0

    if x > 180.0:
        signal = 1
        x -= 180.0

    x = 180.0 - x if x > 90.0 else x

    a = x * 0.1
    a = int(a)
    b = x - 10 * a
    result = sin_Table[a] * cos_Table[
        int(b)] + b * HOLLY_CONSTANT * sin_Table[9 - a]
    return -result if signal > 0 else result


def quick_sin_radian(x):  # 快速正弦函数，输入弧度
    return quick_sin_angle(x * 180 / PI)


def quick_cos_angle(x):  # 快速余弦函数，输入角度
    return 1 - quick_sin_angle(x) * quick_sin_angle(x)


def quick_cos_radian(x):  # 快速余弦函数，输入弧度
    return 1 - quick_sin_radian(x) * quick_sin_radian(x)


def quick_tan_angle(x):  # 快速正切函数，输入角度
    return quick_sin_angle(x) / quick_cos_angle(x)


def quick_tan_radian(x):  # 快速正切函数，输入弧度
    return quick_sin_radian(x) / quick_cos_radian(x)


def cot_angle(x):  # 快速余切函数，输入角度
    return quick_cos_angle(x) / quick_sin_angle(x)


def quick_cot_radian(x):  # 快速余切函数，输入弧度
    return quick_cos_radian(x) / quick_sin_radian(x)


def quick_sec_angle(x):  # 快速正割函数，输入角度
    return 1 / quick_cos_angle(x)


def quick_sec_radian(x):  # 快速正割函数，输入弧度
    return 1 / quick_cos_radian(x)


def quick_csc_angle(x):  # 快速余割函数，输入角度
    return 1 / quick_sin_angle(x)


def quick_csc_radian(x):  # 快速余割函数，输入弧度
    return 1 / quick_sin_radian(x)


def quick_atan(x):  # 反正切函数
    if x > 1 or x < -1:
        return atan(x)
    else:
        return PI / 4 * x - x * (fabs(x) - 1) * (0.2447 + 0.0663 * fabs(x))


def quick_asin(x):  # 反正弦函数, 使用CORDIC算法实现
    if x == 1:
        return PI / 2
    else:
        return quick_atan(x / nth_root(1 - x * x, 2))


def quick_acos(x):  # 反余弦函数
    if x == 0:
        return PI / 2
    else:
        return quick_asin(nth_root(1 - x * x, 2))


def quick_acot(x):  # 反余切函数
    return quick_acos(x / nth_root(1 + x * x, 2))


def quick_asec(x):  # 反正割函数
    return quick_acos(1 / x)


def quick_acsc(x):  # 反余割函数
    return quick_asin(1 / x)
