
def calculator(log: str) -> str:
    match log:
        case str(information) if len(information) < 1:
            print(f"0")
            return f"0"


        case str(infirmation):
            class CalcInit:
                def __init__(self, inf):
                    self.inf = inf
                    self.inf_init = []
                    self.inf_init_upd = []
                    self.inf_construct = []
                    self.inf_upd = []
                    self.result = 0
                    self.more_arg = ""
                    self.first_arg = 0
                    self.second_arg = 0
                    self.symbol_lst = ["+", "-", "="]

                def init_analiz(self):
                    for _, __ in enumerate(self.inf):
                        if __ in self.symbol_lst and len(self.more_arg) < 1:
                            self.inf_init.append(__)
                        elif __ not in self.symbol_lst:
                            self.more_arg += __
                        elif __ in self.symbol_lst:
                            self.inf_init.append(int(self.more_arg))
                            self.more_arg = ""
                            self.inf_init.append(__)
                    if len(self.more_arg) >= 1:
                        self.inf_init.append(int(self.more_arg))
                        self.more_arg = ""
                    for _, __ in enumerate(self.inf_init):
                        if len(self.inf_init_upd) < 1:
                            if __ == "-":
                                self.more_arg = "-"
                            elif __ == "=" or __ == "+" and self.more_arg == "-":
                                self.more_arg = ""
                            elif __ not in self.symbol_lst:
                                self.more_arg += str(__)
                                self.inf_init_upd.append(int(self.more_arg))
                                self.more_arg = ""
                        else:
                            if __ not in self.symbol_lst:
                                self.inf_init_upd.append(self.more_arg)
                                self.more_arg = ""
                                self.inf_init_upd.append(__)
                            elif __ == "-" or "+":
                                self.more_arg = __
                            elif __ == "=" and len(self.more_arg) < 1:
                                self.inf_init_upd.append(__)
                            elif __ == "=" and self.more_arg == "-" or "+" or "=":
                                self.inf_init_upd.append(self.more_arg)
                                self.inf_init_upd.append(__)
                                self.more_arg = ""
                    # self.inf_init_upd.append(self.more_arg)








                def init_inf_init_construct(self):
                    pass






                # def analize(self):
                #     if len(self.inf) == 1 and self.inf[0] in self.symbol_lst:
                #         self.inf_upd.append(0)
                #     else:
                #         for _, __ in enumerate(self.inf):
                #             if len(self.inf) == 1 and __ in self.symbol_lst:
                #                 self.inf_upd.append(0)
                #             elif __ == " ":
                #                 pass
                #             elif __ in self.symbol_lst and len(self.more_arg) < 1:
                #                 if __ == "-":
                #                     self.more_arg += __
                #                 # else:
                #                 #     pass
                #             elif __ not in self.symbol_lst:
                #                 self.more_arg += __
                #             elif __ in self.symbol_lst and _ == len(self.inf) - 1:
                #                 pass
                #             elif __ in self.symbol_lst and len(self.more_arg) >= 1:
                #                 self.inf_upd.append(int(self.more_arg))
                #                 self.inf_upd.append(__)
                #                 self.more_arg = ""
                #         self.inf_upd.append(int(self.more_arg))
                #         if __ in self.symbol_lst and _ == len(self.inf) - 1:
                #             self.inf_upd.append(__)




                def calculation(self):
                    if len(self.inf_upd) == 1:
                        self.result = str(self.inf_upd[0])
                    else:
                        self.result = self.inf_upd[0]
                        for _, __ in enumerate(self.inf_upd):
                            if __ == "+" and len(self.inf_upd) >= _ + 3:
                                if self.inf_upd[_ + 2] in self.symbol_lst:
                                    self.result += self.inf_upd[_ + 1]
                            elif __ == "+" and len(self.inf_upd) >= _ + 2:
                                self.result = self.inf_upd[_ + 1]
                            elif __ == "-" and len(self.inf_upd) >= _ + 3:
                                if self.inf_upd[_ + 2] in self.symbol_lst:
                                    self.result -= self.inf_upd[_ + 1]
                            elif __ == "-" and len(self.inf_upd) >= _ + 2:
                                self.result = self.inf_upd[_ + 1]
                            elif __ == "-" and len(self.inf_upd) >= _ + 4:
                                self.result = self.inf_upd[_ + 3]
                            elif __ == "=" and len(self.inf_upd) >= _ + 3:
                                if self.inf_upd[_ + 2] in self.symbol_lst:
                                    self.result = self.inf_upd[_ + 1]
                            if __ == "=" and len(self.inf_upd) == _ + 2:
                                self.result = self.inf_upd[_ + 1]
            cac = CalcInit(infirmation)
            cac.init_analiz()
            print(cac.inf_init)
            print(cac.inf_init_upd)
            # cac.analize()
            # print((f"{cac.inf_upd}"))
            # cac.calculation()
            # print(f"{str(cac.result)}")
            # return str(cac.result)


        case _:
            print(f"Непредвиденная ошбка нуэен дополнительный анализ.")

calculator("3+=")
# "6"
calculator("3+2==")
# "7"
calculator("3+-2=")
# "1"
calculator("-=-+3-++--+-2=-")
# "1"
# calculator("000000")
# "0"
# calculator("0000123")
# "123"
# calculator("12")
# "12"
# calculator("+12")
# "12"
# calculator("")
# "0"
# calculator("1+2")
# "2"
# calculator("2+")
# "2"
# calculator("1+2=")
# "3"
# calculator("1+2-")
# "3"
# calculator("1+2=2")
# "2"
# calculator("=5=10=15")
# "15"





