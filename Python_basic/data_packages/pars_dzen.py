import requests
from bs4 import BeautifulSoup as bs


class Radio:

    def __init__(self):
        self.url = "http://c.hotcharts.net/"
        self.response = requests.get(self.url)

    def top_list(self):
        if self.response.status_code == 200:
            html_doc = bs(self.response.text, features="html.parser")
            station_name = html_doc.find_all("span", {"class": "title"})
            print(f"The most popular radio station:")
            for number, item in enumerate(station_name):
                print(f"{number + 1}  {item.text:<15}")
        else:
            print(f"Some Error {self.response.status_code}")

    def run(self):
        self.top_list()

radio = Radio()
radio.run()


# url = f"https://dzen.ru/"
# response = requests.get(url)
# if response.status_code == 200:
#     html_doc = bs(response.text, features="html.parser")
# else:
#     print(f"Some Error {response.status_code}")
