


class PrimeNumbers:

    def __init__(self, number):
        self.number = number
        self.lst_prime_numbers = []


    def __call__(self, *args, **kwargs):

        for num in range(2, self.number+1):
            for prime in self.lst_prime_numbers:
                if num % prime == 0:
                    break
                else:
                    self.lst_prime_numbers.append(num)
                    yield num





prime_number_iterator = PrimeNumbers(10000)
print(type(prime_number_iterator))
# for _ in prime_number_iterator:
#     print(_)






# prime_number_iterator = PrimeNumbers(10000)
# for _ in prime_number_iterator:
#     print(_)



