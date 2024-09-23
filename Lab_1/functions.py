# задание с графиком

import time
import matplotlib.pyplot as plt
import numpy as np
import math

# Функции для тестирования
def linear_function(n):
    return n

def quadratic_function(n):
    return n * n

def logarithmic_function(n):
    return math.log(n)

def constant_function(n):
    return 1

def linear_sum_function(n):
    return sum(range(1, n + 1))

# Функция для измерения времени выполнения
def measure_time(func, n, runs=5):
    times = []
    for _ in range(runs):
        start_time = time.time()
        func(n)
        end_time = time.time()
        times.append(end_time - start_time)
    return np.mean(times)

# Параметры
N = 5
max_n = 10**5
step = 100 * N

# Списки для хранения результатов
n_values = list(range(1, max_n + 1, step))
linear_times = []
quadratic_times = []
logarithmic_times = []
constant_times = []
linear_sum_times = []

# Измерение времени выполнения для каждого n
for n in n_values:
    linear_times.append(measure_time(linear_function, n))
    quadratic_times.append(measure_time(quadratic_function, n))
    logarithmic_times.append(measure_time(logarithmic_function, n))
    constant_times.append(measure_time(constant_function, n))
    linear_sum_times.append(measure_time(linear_sum_function, n))

# Построение графика
plt.figure(figsize=(10, 10))
plt.plot(n_values, linear_times, label='Linear Function (O(n))')
plt.plot(n_values, quadratic_times, label='Quadratic Function (O(n^2))')
plt.plot(n_values, logarithmic_times, label='Logarithmic Function (O(log(n)))')
plt.plot(n_values, constant_times, label='Constant Function (O(1))')
plt.plot(n_values, linear_sum_times, label='Linear Sum Function (O(n))')

plt.xlabel('n')
plt.ylabel('Average Execution Time (seconds)')
plt.title('Execution Time vs. n')
plt.legend()
plt.grid(True)
plt.show()