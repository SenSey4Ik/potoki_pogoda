from threading import Thread
import requests
from bs4 import BeautifulSoup
import time
import asyncio
import aiohttp
from multiprocessing import Process

stat_time = time.time()
async def zapros():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://www.meteovesti.ru/pogoda_10/29947') as response:
            return await response.text()


async def parcer():
        html = await zapros()
        soup = BeautifulSoup(html, 'lxml')
        data = soup.find('span', class_="_h3 align-top me-1 d-inline-block").text
        print(f"В Бийске {data} градусов!")





th1 = Thread(target=parcer(), daemon=True)
loop = asyncio.get_event_loop()
tasks1 = [loop.create_task(parcer()) for x in range(25)]
loop.run_until_complete(asyncio.wait(tasks1))
th1.start()
th1.join()



th2 = Thread(target=parcer(), daemon=True)
loop = asyncio.get_event_loop()
tasks2 = [loop.create_task(parcer()) for x in range(25)]
loop.run_until_complete(asyncio.wait(tasks2))
th2.start()
th2.join()

th3 = Thread(target=parcer(), daemon=True)
loop = asyncio.get_event_loop()
tasks3 = [loop.create_task(parcer()) for x in range(25)]
loop.run_until_complete(asyncio.wait(tasks3))
th3.start()
th3.join()


th4 = Thread(target=parcer(), daemon=True)
loop = asyncio.get_event_loop()
tasks4 = [loop.create_task(parcer()) for x in range(25)]
loop.run_until_complete(asyncio.wait(tasks4))
th4.start()
th4.join()

end_time = time.time() - stat_time
print(f'Время выполнения программы {end_time}')