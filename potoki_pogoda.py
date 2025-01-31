from threading import Thread
import requests
from bs4 import BeautifulSoup
import time
import asyncio
import aiohttp
from multiprocessing import Process
import multiprocessing

stat_time = time.time()
def sinh_pog():
    session = requests.Session()
    """Синхронно вызываем get запрос 100 раз"""

    #Ссылка на сайт
    url='https://www.meteovesti.ru/pogoda_10/29947'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
    }

    for i in range(25):
        #Отправляем запрос на сайт с командой получить
        response = session.get(url, headers=headers)

        # просим у сайта вернуть красиво отформатированный текст
        soup = BeautifulSoup(response.text, 'lxml')

        #Парсим класс в котором хранится погода
        data = soup.find('span', class_="_h3 align-top me-1 d-inline-block").text

        print(f'В Бийске{data} градусов')



th1 = Thread(target=sinh_pog(), daemon=True)
th2 = Thread(target=sinh_pog(), daemon=True)
th3 = Thread(target=sinh_pog(), daemon=True)
th4 = Thread(target=sinh_pog(), daemon=True)

th1.start()
th2.start()
th3.start()
th4.start()

th1.join()
th2.join()
th3.join()
th4.join()


end_time = time.time() - stat_time
print(f'Время выполнения программы {end_time}')