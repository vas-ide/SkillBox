#
# 15.06 Практика
#

# Задача: подсчитать выплату суточных агенту 007.
#
# Дано: файл с зашифрованными посланиями, в которых содержатся информация о датах, городах и потраченных суммах:
# external_data/Bond.json
#
# Шифр следующий:
# в каждом послании среди случайных символов содержатся:
# - дата в формате "jbdDDMMYY"
# - город в формате "jbcCITYNAMEjbc"
# - сумма потраченных за день денег в местной валюте в формате "jbeFLOATjbe"
#
# Требуется: составить два файла с тратами по дням, и по месяцам для бухгалтерии МИ-6.

import json
import re
import csv
from pprint import pprint
from datetime import datetime
from decimal import Decimal, ROUND_HALF_EVEN


class Bond:

    def __init__(self, information):
        self.information = information
        self.re_date = r'jbd(\d{6})'
        self.re_city = r'jbc(\w+)jbc'
        self.re_money = r'jbe(\d+\.\d+)jbe'
        self.exchanges = {
            'лондон': Decimal(1.0),  # фунт -> фунт
            'берлин': Decimal(0.87),  # евро -> фунт
            'москва': Decimal(0.12),  # рубли -> фунт
            'токио': Decimal(0.7),  # японские йены -> фунт
        }
        self.analizing_lst = []

    def analize(self):
        with open(self.information, 'r', encoding="utf8") as file_with_data:
            data = json.load(file_with_data)

        for key, value in data.items():
            date = datetime.strptime(re.search(self.re_date, value)[1], "%d%m%y").strftime("%Y-%m-%d")
            city = re.search(self.re_city, value)[1]
            maney = Decimal(re.search(self.re_money, value)[1]) * self.exchanges[city]
            self.analizing_lst.append([date, city, maney])

    def run(self):
        self.analize()
        pprint(self.analizing_lst)

bond = Bond('external_data/Bond.json')
bond.run()
