"""Імпорта"""
import lxml
import requests
from bs4 import BeautifulSoup
"""Модефікатори"""
URL = "https://quotes.toscrape.com/"# сторінка яку будем парсить

HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, '#даємо сайту інформацію 
                                'like Gecko) Chrome/91.0.4472.114 Safari/537.36',# про нас
            'accept': '*/*'
}

"""Функції"""
def get_html(url, params=None):# Отримання коду сторінки
    response = requests.get(url, headers=HEADERS, params=params)# відправляєм запит на сервер
    return response

def get_content():# тут робим сам парсинг/витягуєм дані з сайту
    html = get_html(URL)
    if html.status_code == 200:
        soup = BeautifulSoup(html.text, "lxml")# беремо дані
        products = []# створюєм список вякий будем ложить тещо спарсили назву товару
        items = soup.find_all("span", class_="text", itemprop="text")
        i=0
        for item in items:
            i+=1
            products.append(item.text[1:-1] + "     END     ")
        print(products)
        print(i)
    else:
        print(html.status_code)


"""Запуск/виведення"""
get_content()# тепер запускаєм інформацію по отриманні інвормацію товару назву силку та ціну