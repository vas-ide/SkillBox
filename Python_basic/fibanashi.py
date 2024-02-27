# Еще пример: последовательность Фибоначчи - https://goo.gl/PoqS7
# Последовательность, в которой каждое последующее число равно сумме двух предыдущих чисел:
# 0, 1, 1, 2, 3, 5, 8, pillow_ticket, 21, 34, 55, 89, 144, 233, 377, 610, ...
def fibonacci(n):
    result = []
    a, b = 0, 1
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result


for value in fibonacci(n=10):
    print(value)
# Для больших N функция создаст в памяти огромный список и вернет его - нерационально!


# Сделаем итератор, который будет вычислять следующее значение по требованию (lazy evaluation https://goo.gl/7fzXuA)
class Fibonacci:
    """Итератор последовательности Фибоначчи до N элементов"""

    def __init__(self, n):
        self.i, self.a, self.b, self.n = 0, 0, 1, n

    def __iter__(self):
        self.i, self.a, self.b = 0, 0, 1
        return self

    def __next__(self):
        self.i += 1
        if self.i > 1:
            if self.i > self.n:
                raise StopIteration()
            self.a, self.b = self.b, self.a + self.b
        return self.a


fib_iterator = Fibonacci(10)
print(fib_iterator)
for value in fib_iterator:
    print(value)
print(13 in fib_iterator)
# Каждое значение вычисляется "по месту" - тогда, когда оно понадобилось.