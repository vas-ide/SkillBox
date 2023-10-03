import os
import csv
from collections import defaultdict
import operator
from threading import Thread


class TradersAnaliz(Thread):


    def __init__(self, analiz_data):
        self.analiz_data = analiz_data
        self.data_dict = defaultdict(list)
        self.data_dict_upd = defaultdict(list)
        self.data_dict_max = {}
        self.data_dict_min = {}
        self.lst_zero = []
        self.threads_calc = []
        self.average_price_arr = []
        self.volatility_arr = []

    def run(self):
        for info_in_dir in self.analiz_data:
            if info_in_dir not in self.threads_calc:
                self.threads_calc.append(info_in_dir)
                with open(f"trades/{info_in_dir}", "r", encoding="utf8") as csvfile:
                    reader = csv.reader(csvfile, delimiter=",")
                    for line in reader:
                        self.data_dict[line[0]].append(line[2])

    def preparation(self):
        for key, value in self.data_dict.items():
            if key != "SECID":
                average_price = float(max(value)) + float(min(value)) / 2
                self.data_dict_max[key] = average_price
                volatility = (float(max(value)) - float(min(value)) / float(max(value)) + float(min(value)) / 2) * 100
                self.data_dict_min[key] = round(float(volatility), 2)
                if max(value) == min(value):
                    self.lst_zero.append(key)
        check_items = self.data_dict_max.items()
        max_items = sorted(
            check_items, key=operator.itemgetter(1), reverse=True
        )
        self.average_price_arr = max_items[:3]
        check_items = self.data_dict_min.items()
        max_items = sorted(
            check_items, key=operator.itemgetter(1), reverse=False
        )
        self.volatility_arr = max_items[:3]
        self.lst_zero = sorted(self.lst_zero)

    def printer(self):
        text = "Максимальная"
        print(f"{text:>14} волатильность:")
        for item in self.average_price_arr:
            print(f"{item[0]:>10} - {item[1]}")
        text = "Минимальная"
        print(f"{text:>13} волатильность:")
        for item in self.volatility_arr:
            print(f"{item[0]:>10} - {item[1]}")
        text = "Нулевая"
        print(f"{text:>9} волатильность:")
        print(f"{', '.join(self.lst_zero):>88}")

trader = TradersAnaliz(os.listdir('trades'))
trader.run()
trader.preparation()
trader.printer()
