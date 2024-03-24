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

    def __init__(self, information, path_statistic):
        self.information = information
        self.path_statistic = path_statistic
        self.re_date = r'jbd(\d{6})'
        self.re_city = r'jbc(\w+)jbc'
        self.re_money = r'jbe(\d+\.\d+)jbe'
        self.exchanges = {
            'лондон': Decimal(1.0),  # фунт -> фунт
            'берлин': Decimal(0.87),  # евро -> фунт
            'москва': Decimal(0.12),  # рубли -> фунт
            'токио': Decimal(0.7),  # японские йены -> фунт
        }
        self.swap_cities = {
            'лондон': "London",
            'берлин': "Berlin",
            'москва': "Moscow",
            'токио': "Tokio",
        }
        self.analizing_lst_csv = []
        self.analizing_lst_json = []
        self.month_statistics_dict = {}
        self.month_statistics_lst = []

    def analize(self):
        with open(self.information, 'r', encoding="utf8") as file_with_data:
            data = json.load(file_with_data)

        for key, value in data.items():
            date = datetime.strptime(re.search(self.re_date, value)[1], "%d%m%y").strftime("%Y-%m-%d")
            city = re.search(self.re_city, value)[1]
            money = Decimal(re.search(self.re_money, value)[1]) * self.exchanges[city]
            self.analizing_lst_csv.append({
                "date": date,
                "city": city,
                "money": f"{money.quantize(Decimal('1.00'), ROUND_HALF_EVEN)}",
            })
            self.analizing_lst_json.append({
                'date': date,
                'city': self.swap_cities[city],
                "money": f"{money.quantize(Decimal('1.00'), ROUND_HALF_EVEN)}",
            })
            date_inf = f"{date[:-3]}".strip()
            if date_inf not in self.month_statistics_dict:
                self.month_statistics_dict[date_inf] = money
            else:
                self.month_statistics_dict[date_inf] += money
        for key, value in self.month_statistics_dict.items():
            self.month_statistics_dict[key] = f"{value.quantize(Decimal('1.00'), ROUND_HALF_EVEN)}"

            self.month_statistics_lst.append({
                "date": key,
                "money": f"{value.quantize(Decimal('1.00'), ROUND_HALF_EVEN)}",
            })
    def days_statistics(self):
        with open(f"{self.path_statistic}days_stat.json", 'w', encoding="utf8", newline="") as file_json:
            json.dump(self.analizing_lst_json, file_json, indent=4)
        with open(f"{self.path_statistic}days_stat.csv", 'w', encoding="utf8", newline="") as file_csv:
            writer = csv.DictWriter(file_csv, delimiter=',', fieldnames=['date', 'city', 'money'])
            writer.writeheader()
            writer.writerows(self.analizing_lst_csv)

    def month_statistics(self):
        print(self.analizing_lst_csv)
        print(self.month_statistics_dict)
        with open(f"{self.path_statistic}month_stat.json", 'w', encoding="utf8", newline="") as file_json:
            json.dump(self.month_statistics_dict, file_json, indent=4)
        with open(f"{self.path_statistic}month_stat.csv", 'w', encoding="utf8", newline="") as file_csv:
            writer = csv.DictWriter(file_csv, delimiter=',', fieldnames=['date', 'money'])
            writer.writeheader()
            writer.writerows(self.month_statistics_lst)

    def run(self):
        self.analize()
        self.days_statistics()
        self.month_statistics()


bond = Bond('external_data/Bond.json', '')
bond.run()
