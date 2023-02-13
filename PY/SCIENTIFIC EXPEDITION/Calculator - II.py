
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
                    # self.inf_upd = []
                    self.result = 0
                    self.more_arg = ""
                    self.more_arg_add = ""
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

                def addition_analiz(self):
                    for _, __ in enumerate(self.inf_init):
                        if len(self.inf_init_upd) < 1:
                            if __ == self.symbol_lst[1]:
                                self.more_arg = "-"
                            elif __ == self.symbol_lst[2] or __ == self.symbol_lst[0] and self.more_arg == self.symbol_lst[1]:
                                self.more_arg = ""
                            elif __ not in self.symbol_lst:
                                self.more_arg += str(__)
                                self.inf_init_upd.append(int(self.more_arg))
                                self.more_arg = ""
                        else:
                            if __ not in self.symbol_lst:
                                if self.more_arg != "":
                                    self.inf_init_upd.append(self.more_arg)
                                    self.more_arg = ""
                                self.inf_init_upd.append(__)
                            else:
                                if _ == len(self.inf_init) - 1 and __ in self.symbol_lst:
                                    if self.more_arg == "":
                                        self.inf_init_upd.append(__)
                                    else:
                                        self.inf_init_upd.append(self.more_arg)
                                        self.inf_init_upd.append(__)
                                elif __ != self.symbol_lst[2]:
                                    self.more_arg = __
                                elif __ == self.symbol_lst[2]:
                                    if self.inf_init[_ - 1] not in self.symbol_lst \
                                            and self.inf_init[_ + 1] not in self.symbol_lst:
                                        self.inf_init_upd.append(__)
                                    elif self.more_arg == self.symbol_lst[0] or self.more_arg == self.symbol_lst[1]:
                                        self.inf_init_upd.append(self.more_arg)
                                        self.more_arg = ""
                                        self.inf_init_upd.append(__)
                                    elif self.inf_init_upd[-1] == self.symbol_lst[2]:
                                        self.inf_init_upd.append(__)

                # def construct(self):
                #     for _, __ in enumerate(self.inf_init_upd):
                #         if __ not in self.symbol_lst:
                #             self.inf_construct.append(__)
                #             self.more_arg = __
                #         else:
                #             if _ == len(self.inf_init_upd) - 1 and self.inf_init_upd[-1] == self.symbol_lst:
                #                 self.inf_construct.append(__)
                #             # elif _ == len(self.inf_init_upd) - 1 and self.inf_construct[-1] in self.symbol_lst:
                #             #     self.inf_construct.append(self.more_arg)
                #             elif __ == self.symbol_lst[2] and self.inf_init_upd[_ - 1] in self.symbol_lst:
                #                 self.more_arg_add = self.inf_init_upd[_ - 1]
                #
                #                 self.inf_construct.append(self.more_arg)




                def calculation(self):
                    if len(self.inf_init_upd) == 1:
                        self.result = str(self.inf_init_upd[0])
                    else:
                        self.result = self.inf_init_upd[0]
                        for _, __ in enumerate(self.inf_init_upd):
                            if __ == self.symbol_lst[2] and self.inf_init_upd[_ - 1] not in self.symbol_lst \
                                    and _ != len(self.inf_init_upd) - 1:
                                self.result = self.inf_init_upd[_ + 1]





                # def calculation(self):
                #     if len(self.inf_upd) == 1:
                #         self.result = str(self.inf_upd[0])
                #     else:
                #         self.result = self.inf_upd[0]
                #         for _, __ in enumerate(self.inf_init_upd):
                #             if __ == "+" and len(self.inf_upd) >= _ + 3:
                #                 if self.inf_upd[_ + 2] in self.symbol_lst:
                #                     self.result += self.inf_upd[_ + 1]
                #             elif __ == "+" and len(self.inf_upd) >= _ + 2:
                #                 self.result = self.inf_upd[_ + 1]
                #             elif __ == "-" and len(self.inf_upd) >= _ + 3:
                #                 if self.inf_upd[_ + 2] in self.symbol_lst:
                #                     self.result -= self.inf_upd[_ + 1]
                #             elif __ == "-" and len(self.inf_upd) >= _ + 2:
                #                 self.result = self.inf_upd[_ + 1]
                #             elif __ == "-" and len(self.inf_upd) >= _ + 4:
                #                 self.result = self.inf_upd[_ + 3]
                #             elif __ == "=" and len(self.inf_upd) >= _ + 3:
                #                 if self.inf_upd[_ + 2] in self.symbol_lst:
                #                     self.result = self.inf_upd[_ + 1]
                #             if __ == "=" and len(self.inf_upd) == _ + 2:
                #                 self.result = self.inf_upd[_ + 1]
            cac = CalcInit(infirmation)
            cac.init_analiz()
            cac.addition_analiz()
            print(cac.inf_init)
            print(cac.inf_init_upd)
            # cac.construct()
            # print(cac.inf_construct)
            cac.calculation()
            print(f"{str(cac.result)}")
            return str(cac.result)


        case _:
            print(f"Непредвиденная ошбка нуэен дополнительный анализ.")
calculator("3===+====")
calculator("3+=")
# "6"
calculator("3+2==")
# "7"
calculator("3+-2=")
# "1"
calculator("-=-+3-++--+-2=-")
# "1"
calculator("000000")
# "0"
calculator("0000123")
# "123"
calculator("12")
# "12"
calculator("+12")
# "12"
calculator("")
# "0"
calculator("1+2")
# "2"
calculator("2+")
# "2"
calculator("1+2=")
# "3"
calculator("1+2-")
# "3"
calculator("1+2=2")
# "2"
calculator("=5=10=15")
# "15"





