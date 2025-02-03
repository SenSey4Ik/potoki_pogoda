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


def potok_1():
    stat_time = time.time()
    argyment = 24
    for i in range(1):
        threads = [Thread(target=mnogopotok_pog(argyment))]

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    end_time = time.time() - stat_time
    print(f'Время выполнения программы с одним потоком {end_time}')


def potok_2():
    stat_time = time.time()
    argyment = 12
    for i in range(2):
        threads = [Thread(target=mnogopotok_pog(argyment))]

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    end_time = time.time() - stat_time
    print(f'Время выполнения программы с двумя потоками{end_time}')

def potok_3():
    stat_time = time.time()
    argyment = 8
    for i in range(3):
        threads = [Thread(target=mnogopotok_pog(argyment))]

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    end_time = time.time() - stat_time
    print(f'Время выполнения программы с тремя потоками{end_time}')

def potok_4():
    stat_time = time.time()
    argyment = 6
    for i in range(4):
        threads = [Thread(target=mnogopotok_pog(argyment))]

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    end_time = time.time() - stat_time
    print(f'Время выполнения программы с четыремя потоками{end_time}')

def potok_5():
    stat_time = time.time()
    argyment = 5
    for i in range(5):
        threads = [Thread(target=mnogopotok_pog(argyment))]

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    end_time = time.time() - stat_time
    print(f'Время выполнения программы с пятью потоками {end_time}')

def potok_6():
    stat_time = time.time()
    argyment = 4
    for i in range(6):
        threads = [Thread(target=mnogopotok_pog(argyment))]

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    end_time = time.time() - stat_time
    print(f'Время выполнения программы с шестью потоками{end_time}')

def potok_7():
    stat_time = time.time()
    argyment = 3
    for i in range(7):
        threads = [Thread(target=mnogopotok_pog(argyment))]

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    end_time = time.time() - stat_time
    print(f'Время выполнения программы с семью потоками{end_time}')

def potok_8():
    stat_time = time.time()
    argyment = 3
    for i in range(8):
        threads = [Thread(target=mnogopotok_pog(argyment))]

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    end_time = time.time() - stat_time
    print(f'Время выполнения программы с восьмью потоками{end_time}')






def main():
    potok_1()
    potok_2()
    potok_3()
    potok_4()
    potok_5()
    potok_6()
    potok_7()
    potok_8()


main()
