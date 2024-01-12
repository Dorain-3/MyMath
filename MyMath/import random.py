import random
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定中文字体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

size = 100
x = range(size)
y_values = [random.randint(1, 1000) for _ in range(size)]

y_math = [np.int64(np.square(i)) for i in y_values]

plt.scatter(x, y_values, label='Random Data')
plt.scatter(x, y_math, label='math库函数')

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Random Data and Squared Data')
plt.legend()

plt.show()
