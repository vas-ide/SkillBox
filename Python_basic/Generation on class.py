

# class PrimeNumbers:
#
#     def __init__(self, n):
#         self.n = n
#         self.prime_numbers = []
#
#     def get_prime_numbers(self):
#         for number in range(2, self.n + 1):
#             for prime in self.prime_numbers:
#                 if number % prime == 0:
#                     break
#             else:
#                 self.prime_numbers.append(number)
#                 yield number
#
#
# prime_number_iterator = PrimeNumbers(n=10000).get_prime_numbers()
# for number in prime_number_iterator:
#     print(number)





# def prime_numbers_generator(n):
#         prime_numbers = []
#         for number in range(2, n + 1):
#             for prime in prime_numbers:
#                 if number % prime == 0:
#                     break
#             else:
#                 prime_numbers.append(number)
#                 yield number
#
#
# for number in prime_numbers_generator(n=10000):
#     print(number)