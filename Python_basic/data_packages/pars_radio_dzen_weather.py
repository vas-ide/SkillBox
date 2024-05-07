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


class Dzen:
    def __init__(self):
        self.url = f"https://dzen.ru/"
        self.response = requests.get(self.url)

    def info(self):
        if self.response.status_code == 200:
            html_doc = bs(self.response.content, features="html.parser")
            # block_item = html_doc.find_all(attrs={"class": "header-widgets__rates-ii"})
            # print(block_item)



            # item_name = html_doc.find("a")["currency-rates__rate-fu"]
            # item_value= html_doc.find("a").find("span")["currency-rates__rateValue-2X"]
            # # item_name = html_doc.find_all("span", {"class": "currency-rates__rateValue-2X"})
            # # item_value = html_doc.find_all("div", {"class": "header-widgets__widgetWrapper-1X"})
            # print(f"{item_name}\n{item_value}")


        else:
            print(f"Some Error {self.response.status_code}")

    def run(self):
        self.info()


# dzen = Dzen()
# dzen.run()


class TheWeatherNetworkRostov:
    def __init__(self):
        self.url = f"https://www.theweathernetwork.com/ru/weather/rostovskaya/rostov-na-donu"
        self.response = requests.get(self.url)

    def info(self):
        if self.response.status_code == 200:
            html_doc = bs(self.response.content, features="html.parser")
            block_item = html_doc.find_all("span",{"class": "temp"})
            print(block_item)



            # item_name = html_doc.find("a")["currency-rates__rate-fu"]
            # item_value= html_doc.find("a").find("span")["currency-rates__rateValue-2X"]
            # # item_name = html_doc.find_all("span", {"class": "currency-rates__rateValue-2X"})
            # # item_value = html_doc.find_all("div", {"class": "header-widgets__widgetWrapper-1X"})
            # print(f"{item_name}\n{item_value}")
        else:
            print(f"Some Error {self.response.status_code}")

    def run(self):
        self.info()


rostov = TheWeatherNetworkRostov()
rostov.run()
