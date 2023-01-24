class Multiplier:

    def __init__(self, n):
        self.n = n

    def __call__(self, x):
        # если есть такой метод у класса - то его обьект можно "вызывать" как функцию
        return x * self.n


my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
by_100500 = Multiplier(n=100500)
result = by_100500(x=42)
print(result)

result = map(by_100500, my_numbers)
print(list(result))
