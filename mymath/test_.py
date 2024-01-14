import mymath as math2
import random
import math
import time
import matplotlib.pyplot as plt


plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定中文字体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# size = 10
# # x = range(size)
# # y_values = [random.randint(1, 10) for _ in range(size)]
x_values = [i*0.1 for i in range(-100, 101, 1) ]
# y_values = [i*0.01 for i in range(-100, 101, 1) ]

function_name = math.sin.__name__
y_math = [math.sin(i) for i in x_values]
y_mymath = [math2.sin(i) for i in x_values]

plt.plot(x_values, y_mymath, label='mymath库函数')
plt.plot(x_values, y_math, label='math库函数')

plt.xlabel('输入')
plt.ylabel('输出')
plt.title('mymath库函数和math库函数输出对比('+function_name+')')
plt.legend()

plt.show()
# print(math2.cot(0))
# print(math.log(15000000))
# print(math2.ln(15000000))


# starttime=time.time()
# y_math = [math.sqrt(i) for i in x_values]
# endtime=time.time()

# starttime2=time.time()
# y_mymath = [math2.sqrt(i) for i in x_values]
# endtime2=time.time()

# print(endtime-starttime)
# print(endtime2-starttime2)
