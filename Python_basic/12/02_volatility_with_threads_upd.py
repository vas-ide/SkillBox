import os
import csv
import threading
from collections import defaultdict
import operator
from threading import Thread


class TradersAnaliz(Thread):

    def __init__(self, analiz_data, name, tiker_calc, data_dict, lock, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.analiz_data = analiz_data
        self.name = name
        self.tiker_calc = tiker_calc
        self.data_dict = data_dict
        self.data_dict_lock = lock
        self.local_data_dict = defaultdict(list)

    def run(self):

        for info_in_dir in self.analiz_data:
            if info_in_dir not in self.tiker_calc:
                self.tiker_calc.append(info_in_dir)
                with open(f"trades/{info_in_dir}", "r", encoding="utf8") as csvfile:
                    reader = csv.reader(csvfile, delimiter=",")
                    for line in reader:
                        self.data_dict_lock.acquire()
                        self.data_dict[line[0]].append(line[2])
                        self.data_dict_lock.release()
                        self.local_data_dict[line[0]].append(line[2])


global_tiker_calc = []
global_data_dict = defaultdict(list)

THREADS_CALC = ["calc_1", "calc_2", "calc_3", "calc_4", "calc_5"]
# THREADS_CALC = ["calc_1", "calc_2", "calc_3", "calc_4", "calc_5", "calc_6", "calc_7", "calc_8", "calc_9", "calc_10",
#                 "calc_11"]
lock = threading.Lock()
work_calc_lst = [
    TradersAnaliz(analiz_data=os.listdir('trades'), name=name, tiker_calc=global_tiker_calc, data_dict=global_data_dict,
                  lock=lock)
    for name in THREADS_CALC]

for work_calc in work_calc_lst:
    work_calc.start()
for work_calc in work_calc_lst:
    work_calc.join()

global_local_dict_calc = {}
global_data_dict_calc = [global_local_dict_calc.update(work_calc.local_data_dict) for work_calc in work_calc_lst]


class Display():
    def __init__(self, analiz_data):
        self.data_dict = analiz_data
        self.data_dict_max = {}
        self.data_dict_min = {}
        self.lst_zero = []
        self.average_price_arr = []
        self.volatility_arr = []

    def run(self):
        self.preparation()
        self.printer()

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


# disp = Display(analiz_data=global_data_dict)
disp = Display(analiz_data=global_local_dict_calc)
disp.run()
