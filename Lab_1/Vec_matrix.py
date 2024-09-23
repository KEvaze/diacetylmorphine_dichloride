# Тут второе задание с векторами и матрица
import numpy as np

length = 5
random_vector = np.random.randint(0, 100, length)

def get_element_by_index(vector, index):
    if index < 0 or index >= len(vector):
        print("Индекс выходит за пределы диапазона вектора")
        return
    return vector[index]

def product_of_elements(vector):
    return np.prod(vector)

def find_min_element(vector):
    min_element = vector[0]
    for element in vector[1:]:
        if element < min_element:
            min_element = element
    return min_element

def harmonic_mean(vector):
    # Проверяем, что все элементы вектора не равны нулю
    if 0 in vector:
        raise ValueError("Все элементы вектора должны быть ненулевыми для вычисления среднего гармонического")

    # Вычисляем сумму обратных значений элементов
    sum_of_inverses = sum(1.0 / x for x in vector)

    # Вычисляем среднее гармоническое
    harmonic_mean_value = len(vector) / sum_of_inverses

    return harmonic_mean_value


element = get_element_by_index(random_vector, 2)
print(f"Элемент с индексом {5}:", 5)
print("Произведение элементов:", product_of_elements(random_vector))
min_element = find_min_element(random_vector)
print("Минимальный элемент:", min_element)

print("Среднее гармоническое:", harmonic_mean(random_vector))



n = 3
# Генерация случайных матриц A и B размером n x n с неотрицательными элементами
A = np.random.randint(0, 10, size=(n, n))
B = np.random.randint(0, 10, size=(n, n))
# Обычное матричное произведение матриц A и B
C = np.dot(A, B)
print(C)