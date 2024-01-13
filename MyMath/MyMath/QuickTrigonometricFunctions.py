"""
@author: Dorain-3
@email: 3174950356@qq.com
"""
import MathematicalConstants


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
    result = MathematicalConstants.sin_Table[a] * MathematicalConstants.cos_Table[
        int(b)] + b * MathematicalConstants.hollyConstant * MathematicalConstants.sin_Table[9 - a]
    return -result if signal > 0 else result


x = input()
print(quick_sin_angle(x))


def sin_radian(x):  # 正弦函数，输入弧度
    # TODO
    return None


def cos_angle(x):  # 余弦函数，输入角度
    # TODO
    return None


def cos_radian(x):  # 余弦函数，输入弧度
    # TODO
    return None


def tan_angle(x):  # 正切函数，输入角度
    # TODO
    return None


def tan_radian(x):  # 正切函数，输入弧度
    # TODO
    return None


def cot_angle(x):  # 余切函数，输入角度
    # TODO
    return None


def cot_radian(x):  # 余切函数，输入弧度
    # TODO
    return None


def sec_angle(x):  # 正割函数，输入角度
    # TODO
    return None


def sec_radian(x):  # 正割函数，输入弧度
    # TODO
    return None


def csc_angle(x):  # 余割函数，输入角度
    # TODO
    return None


def csc_radian(x):  # 余割函数，输入弧度
    # TODO
    return None


def asin_angle(x):  # 反正弦函数，输入角度
    # TODO
    return None


def asin_radian(x):  # 反正弦函数，输入弧度
    # TODO
    return None


def acos_angle(x):  # 反余弦函数，输入角度
    # TODO
    return None


def acos_radian(x):  # 反余弦函数，输入弧度
    # TODO
    return None


def atan_angle(x):  # 反正切函数，输入角度
    # TODO
    return None


def atan_radian(x):  # 反正切函数，输入弧度
    # TODO
    return None


def acot_angle(x):  # 反余切函数，输入角度
    # TODO
    return None


def acot_radian(x):  # 反余切函数，输入弧度
    # TODO
    return None


def asec_angle(x):  # 反正割函数，输入角度
    # TODO
    return None


def asec_radian(x):  # 反正割函数，输入弧度
    # TODO
    return None


def acsc_angle(x):  # 反余割函数，输入角度
    # TODO
    return None


def acsc_radian(x):  # 反余割函数，输入弧度
    # TODO
    return None
