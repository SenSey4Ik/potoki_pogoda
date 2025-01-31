from threading import Thread
import requests
from bs4 import BeautifulSoup
import time

stat_time = time.time()
def sinh_pog(i):
    """Синхронно вызываем get запрос 100 раз"""

    #Ссылка на сайт
    url='https://www.meteovesti.ru/pogoda_10/29947'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
    }


    #Отправляем запрос на сайт с командой получить
    response = requests.get(url, headers=headers)

    # просим у сайта вернуть красиво отформатированный текст
    soup = BeautifulSoup(response.text, 'lxml')

    #Парсим класс в котором хранится погода
    data = soup.find('span', class_="_h3 align-top me-1 d-inline-block").text

    print(f'В Бийске{data} градусов')
    print(f'Запущен поток {i}')


for i in range(10):
    th = Thread(target=sinh_pog(i), args=(i,))

th.start()

end_time = time.time() - stat_time
print(f'Время выполнения программы {end_time}')