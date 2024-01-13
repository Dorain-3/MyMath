import sys
import mymath as math2
import random
import math
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定中文字体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

size = 10
# x = range(size)
# y_values = [random.randint(1, 10) for _ in range(size)]
# x_values = [i for i in np.arange(2, 3, 0.001) ]
# y_values = [i for i in np.arange(2, 3, 0.001) ]
# function_name = math.log.__name__
# y_math = [math.log(i,j) for i in x_values for j in y_values]
# y_mymath = [math2.log(i,j) for i in x_values for j in y_values]

# plt.plot(x_values, y_mymath, label='mymath库函数')
# plt.plot(x_values, y_math, label='math库函数')

# plt.xlabel('输入')
# plt.ylabel('输出')
# plt.title('mymath库函数和math库函数输出对比('+"function_name"+')')
# plt.legend()

# plt.show()
print(math2.ln(1))