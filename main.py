from collections import deque

# Задание 1.
def is_even(value):
    return (value & 1) == 0
# Преймущество данного метода в скорости исполнения так как тут сравнивается толькое еденица или ноль в конце. 
# В вашем методе главное преймущество, это читабельность кода человек незнакомый с побитовым сравнением скорее всего легко прочитает данный код.
# Задание 2.
# Циклический буфер на основе списка
class CircularBufferList:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = [None] * capacity
        self.head = 0
        self.size = 0

    def append(self, item):
        self.buffer[self.head] = item
        if self.size < self.capacity:
            self.size += 1
        self.head = (self.head + 1) % self.capacity

    def pop(self):
        if self.size == 0:
            raise IndexError("Попытка извлечь из пустого буфера")
        tail_index = (self.head - self.size + self.capacity) % self.capacity
        item = self.buffer[tail_index]
        self.buffer[tail_index] = None  # Очистка значения
        self.size -= 1
        return item

    def __len__(self):
        return self.size

    def __str__(self):
        return str(self.buffer)
# Циклический буфер на основе dequefrom collections import deque

class CircularBufferDeque:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = deque(maxlen=capacity)

    def append(self, item):
        self.buffer.append(item)

    def pop(self):
        if len(self.buffer) == 0:
            raise IndexError("Попытка извлечь из пустого буфера")
        return self.buffer.popleft()

    def __len__(self):
        return len(self.buffer)

    def __str__(self):
        return str(self.buffer)
# Плюсы и минусы реализации на основе списка:
    #Плюсы:
        # Простой и понятный код.
        # Имеется контроль над памятью и структурой буфера.
    # Минусы:
        # Менее эфективное извление элемента по сравнению с deque.
# Плюсы и минусы реализации на основе deque:
    # Плюсы:
        # Удобное удаление и добавление с обоих концов.
        # Более короткий код.
    # Минусы:
        # Нужно больше ресурсов.
        # Меньший контроль над памятью.
# Быстродействие
    # Сложность операций:
        # deque более быстрый на удаление и добавление данных.
# Заключение
    # Если нужна производительность то лучше deque. Если более простой код то список.
# Задача 3.
def sort_array(arr):
    return sorted(arr)
# Я считаю данную функцию самой оптимальной поскольку она является встроенной функцие языка, проверенна временем. В хушем случае ее скорость равна(О(n log n)),
# что хорошо для обработки больших массивов а если массив отартирован то скорость О(n). Сама по себе функция очень проста и понятна, то довольно важно для 
# читаемости кода. Стабильный алгоритм сортировки.