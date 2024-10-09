import time
import matplotlib.pyplot as plt
import numpy as np
import math

# Функции для тестирования с фиксированной задержкой
def cubic_function(n, delay):
    time.sleep(delay)
    return n * n * n

def exponential_function(n, delay):
    time.sleep(delay)
    return 2 ** n

def factorial_function(n, delay):
    time.sleep(delay)
    return math.factorial(n)

def square_root_function(n, delay):
    time.sleep(delay)
    return math.sqrt(n)

# Функция для измерения времени выполнения
def measure_time(func, n, delay, runs=5):
    times = []
    for _ in range(runs):
        start_time = time.time()
        func(n, delay)
        end_time = time.time()
        times.append(end_time - start_time)
    return np.mean(times)

# Параметры
N = 20 - 5
max_n = 10**5 * N
step = 100 * N
delay = 0.001  # Фиксированная задержка в секундах

# Списки для хранения результатов
n_values = list(range(1, max_n + 1, step))
cubic_times = []
exponential_times = []
factorial_times = []
square_root_times = []

# Измерение времени выполнения для каждого n
for n in n_values:
    cubic_times.append(measure_time(cubic_function, n, delay))
    exponential_times.append(measure_time(exponential_function, n, delay))
    factorial_times.append(measure_time(factorial_function, n, delay))
    square_root_times.append(measure_time(square_root_function, n, delay))

# Построение графика
plt.figure(figsize=(10, 10))
plt.plot(n_values, cubic_times, label='Cubic Function (O(n^3))')
plt.plot(n_values, exponential_times, label='Exponential Function (O(2^n))')
plt.plot(n_values, factorial_times, label='Factorial Function (O(n!))')
plt.plot(n_values, square_root_times, label='Square Root Function (O(sqrt(n)))')

plt.xlabel('n')
plt.ylabel('Average Execution Time (seconds)')
plt.title('Execution Time vs. n')
plt.legend()
plt.grid(True)
plt.show()