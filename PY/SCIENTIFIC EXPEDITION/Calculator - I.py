
def calculator(log: str) -> str:
    match log:
        case str(infirmation):
            class CalcInit:
                def __init__(self, inf):
                    self.inf = inf
                    self.result = 0
                    self.first_arg = 0
                    self.second_arg = 0
                    self.symbol_lst = ["+", "-", "="]

                def calculation(self):
                    for _, __ in enumerate(self.inf):
                        if __ == "0" and self.result == 0:
                            pass
                        elif self.result == 0 and __ not in self.symbol_lst:
                            self.result = int(__)
                        else:
                            if __ == "+" and _ != 0:
                                self.first_arg = int(self.inf[_ + 1])
                                self.result += self.first_arg
                                self.first_arg = 0
                            elif __ == "-" and _ != 0:
                                self.first_arg = int(self.inf[_ + 1])
                                self.result -= self.first_arg
                                self.first_arg = 0
            cac = CalcInit(infirmation)
            cac.calculation()
            print(f"{cac.result}")

            # def addition(self):
            #     self.result = self.result + self.first_arg
            # def subtraction(self):
            #     self.result = self.result - self.first_arg
            # def equals(self):
            #     self.result = self.result + self.first_arg


        case _:
            print(f"Непредвиденная ошбка нуэен дополнительный анализ.")
calculator("5+5")
calculator("10-5")



#
# assert calculator("000000")
# # "0"
# assert calculator("0000123")
# # "123"
# assert calculator("12")
# # "12"
# assert calculator("+12")
# # "12"
# assert calculator("")
# # "0"
# assert calculator("1+2")
# # "2"
# assert calculator("2+")
# # "2"
# assert calculator("1+2=")
# # "3"
# assert calculator("1+2-")
# # "3"
# assert calculator("1+2=2")
# # "2"
# assert calculator("=5=10=15")
# # "15"
#
#
#

