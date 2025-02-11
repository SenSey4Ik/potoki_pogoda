from threading import Thread, Event
import requests
from bs4 import BeautifulSoup
import time
import asyncio
import aiohttp
from multiprocessing import Process
import multiprocessing




def mnogopotok_pog(argyment):
    """Вызов погоды многопоточно"""

    #Подключаемся к сессии
    session = requests.Session()

    #Ссылка на сайт
    url='https://www.meteovesti.ru/pogoda_10/29947'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
    }

    for i in range(argyment):

        #Отправляем запрос на сайт с командой получить
        response = session.get(url, headers=headers)

        # просим у сайта вернуть красиво отформатированный текст
        soup = BeautifulSoup(response.text, 'lxml')

        #Парсим класс в котором хранится погода
        data = soup.find('span', class_="_h3 align-top me-1 d-inline-block").text

        print(f'В Бийске{data} градусов')


def potok_1(kol_pot, argyment):
    stat_time = time.time()
    for i in range(kol_pot):
        threads = [Thread(target=mnogopotok_pog(argyment))]

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    end_time = time.time() - stat_time
    print(f'Время выполнения программы с {kol_pot} потоком {end_time}')




def main():
    potok_1(1,24)
    potok_1(2,12)
    potok_1(3,8)
    potok_1(4,6)
    potok_1(5,5)
    potok_1(6,4)
    potok_1(7,3)
    potok_1(8,3)


main()
