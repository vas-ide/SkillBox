
import re
def calculator(log: str) -> str:
    match log:
        case str(infirmation):
            class CalcInit:
                def __init__(self, inf):
                    self.inf = inf
                    self.inf_upd = []
                    self.result = 0
                    self.more_arg = ""
                    self.first_arg = 0
                    self.symbol_lst = ["+", "-", "="]


                def analize(self):
                    for _, __ in enumerate(self.inf):
                        if __ == "0" and len(self.more_arg) < 1:
                            pass
                        elif __ == " ":
                            pass
                        elif __ in self.symbol_lst and len(self.more_arg) < 1:
                            if __ == "-":
                                self.more_arg += __
                            else:
                                pass
                        elif __ not in self.symbol_lst:
                            self.more_arg += __
                        elif __ in self.symbol_lst and _ == len(self.inf) - 1:
                            break
                        elif __ in self.symbol_lst and len(self.more_arg) >= 1:
                                self.inf_upd.append(int(self.more_arg))
                                self.inf_upd.append(__)
                                self.more_arg = ""
                    self.inf_upd.append(int(self.more_arg))


                def calculation(self):
                    if len(self.inf_upd) == 1:
                        self.result = self.inf_upd[0]
                    else:
                        self.result = self.inf_upd[0]
                        for _, __ in enumerate(self.inf_upd):
                            if __ == "+":
                                self.result += self.inf_upd[_ + 1]
                            elif __ == "-":
                                self.result -= self.inf_upd[_ + 1]
                            elif __ == "=":
                                self.first_arg = self.inf_upd[0]
                                self.result += self.first_arg

            cac = CalcInit(infirmation)
            cac.analize()
            print((f"{cac.inf_upd}"))
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
calculator(" -1 + - 2")



#
# assert calculator("000000")
# # "0"
assert calculator("0000123")
# # "123"
assert calculator("12")
# # "12"
assert calculator("+12")
# # "12"
assert calculator("-12")
# # "-12"
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
