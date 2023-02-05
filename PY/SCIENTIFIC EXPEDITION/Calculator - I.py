
def calculator(log: str) -> str:
    match log:
        case str(information) if len(information) < 1:
            print(f"0")
            return f"0"


        case str(infirmation):
            class CalcInit:
                def __init__(self, inf):
                    self.inf = inf
                    self.inf_upd = []
                    self.result = 0
                    self.more_arg = ""
                    self.first_arg = 0
                    self.second_arg = 0
                    self.symbol_lst = ["+", "-", "="]


                def analize(self):
                    for _, __ in enumerate(self.inf):
                        if __ == " ":
                            pass
                        elif __ in self.symbol_lst and len(self.more_arg) < 1:
                            if __ == "-":
                                self.more_arg += __
                            else:
                                pass
                        elif __ not in self.symbol_lst:
                            self.more_arg += __
                        elif __ in self.symbol_lst and _ == len(self.inf) - 1:
                            pass
                        elif __ in self.symbol_lst and len(self.more_arg) >= 1:
                                self.inf_upd.append(int(self.more_arg))
                                self.inf_upd.append(__)
                                self.more_arg = ""
                    self.inf_upd.append(int(self.more_arg))
                    if __ in self.symbol_lst and _ != len(self.inf) - 1:
                        self.inf_upd.append(__)




                def calculation(self):
                    if len(self.inf_upd) == 1:
                        self.result = str(self.inf_upd[0])
                    else:
                        self.result = self.inf_upd[0]
                        for _, __ in enumerate(self.inf_upd):
                            if __ == "+" and self.inf[-1] in self.symbol_lst:
                                self.result += self.inf_upd[_ + 1]
                            elif __ == "-" and self.inf[-1] in self.symbol_lst:
                                self.result -= self.inf_upd[_ + 1]
                            elif __ == "=":
                                self.result = self.inf_upd[_ + 1]

            cac = CalcInit(infirmation)
            cac.analize()
            print((f"{cac.inf_upd}"))
            cac.calculation()
            print(f"{str(cac.result)}")
            return str(cac.result)


        case _:
            print(f"Непредвиденная ошбка нуэен дополнительный анализ.")

#
calculator("000000")
# # "0"
calculator("0000123")
# # "123"
calculator("12")
# # "12"
calculator("+12")
# # "12"
calculator("")
# # "0"
calculator("1+2")
# # "2"
calculator("2+")
# # "2"
calculator("1+2=")
# # "3"
calculator("1+2-")
# # "3"
calculator("1+2=2")
# # "2"
calculator("=5=10=15")
# # "15"




