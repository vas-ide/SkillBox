import os
import csv
from collections import defaultdict
import operator
from threading import Thread


class TradersAnaliz(Thread):

    def __init__(self, analiz_data, name, tiker_calc, data_dict, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.analiz_data = analiz_data
        self.name = name
        self.threads_calc = tiker_calc
        self.data_dict = data_dict
        # self.data_dict_upd = defaultdict(list)
        # self.data_dict_max = {}
        # self.data_dict_min = {}
        # self.lst_zero = []

        # self.average_price_arr = []
        # self.volatility_arr = []
        # self.lock_sft = lock

    def run(self):
        for info_in_dir in self.analiz_data:
            print(info_in_dir)
            if info_in_dir not in self.threads_calc:
                self.threads_calc.append(info_in_dir)
                with open(f"trades/{info_in_dir}", "r", encoding="utf8") as csvfile:
                    reader = csv.reader(csvfile, delimiter=",")
                    for line in reader:
                        # print(line)
                        # self.lock_sft.acqure()
                        self.data_dict[line[0]].append(line[2])
                        # self.lock_sft.reliase()


global_tiker_calc = []
global_data_dict = defaultdict(list)

THREADS_CALC = ["calc_1", "calc_2", "calc_3", "calc_4", "calc_5"]
# THREADS_CALC = ["calc_1", "calc_2", "calc_3", "calc_4", "calc_5", "calc_6", "calc_7", "calc_8", "calc_9", "calc_10",
#                 "calc_11"]
work_calc_lst = [
    TradersAnaliz(analiz_data=os.listdir('trades'), name=name, tiker_calc=global_tiker_calc, data_dict=global_data_dict)
    for name in THREADS_CALC]

def run_in_threads():
    for work_calc in work_calc_lst:
        work_calc.start()
    for work_calc in work_calc_lst:
        work_calc.join()

print(global_data_dict)


