import asyncio
import time
import random

start_time = time.time()
trains = asyncio.Queue()
stations = []


class Train:
    def __init__(self, number):
        self.free_place = 200
        self.time_go = {'Рокоссовская': 6, 'Соборная': 3, 'Кристалл': 2, 'Заречная': 7,
                        'Библиотека имени Пушкина': 0}
        self.number = number
        self.current = ''
        self.id = 0

    async def bring_people(self, st):
        people_on_s = st.people
        self.free_place += random.randint(0, 200 - self.free_place)
        self.id += 1
        await st.control(self.number, self.free_place)
        if people_on_s > self.free_place:
            self.free_place = 0
        else:
            self.free_place = self.free_place - people_on_s
        await asyncio.sleep(0.15)
        print('Поезд произвёл посадку и высадку пассажиров')
        if self.current == 'Библиотека имени Пушкина':
            print('Поезд завершил свою поездку')

    async def train_go(self, st):
        print('Поезд движется на следующую станцию')
        await self.bring_people(st)
        await asyncio.sleep(self.time_go.get(st.name))


class Station:

    def __init__(self, name):
        self.name = name
        self.people = 0

    async def control(self, number, free_place):
        print(f"Поезд {number} прибыл на станцию {self.name}")
        self.people = self.people - free_place if self.people > free_place else 0

    async def passengers(self):
        while True:
            self.people += 50
            await asyncio.sleep(1)
            print(f"Людей на станци {self.name} {self.people}")


async def trains_online():
    num = 0
    while True:
        num += 1
        train = Train(num)
        await trains.put(train)
        await asyncio.sleep(3)


async def main():
    while True:
        train = await trains.get()
        st = stations[train.id]
        await train.train_go(st)
        if st.name != 'Библиотека имени пушкина':
            await trains.put(train)


Rok = Station('Рокоссовская')
Sob = Station('Соборная')
Cry = Station('Кристалл')
Zar = Station('Заречная')
Lib = Station('Библиотека имени Пушкина')
stations.append(Rok)
stations.append(Sob)
stations.append(Cry)
stations.append(Zar)
stations.append(Lib)

loop = asyncio.get_event_loop()
loop.create_task(Rok.passengers())
loop.create_task(Sob.passengers())
loop.create_task(Cry.passengers())
loop.create_task(Zar.passengers())
loop.create_task(Lib.passengers())
loop.create_task(trains_online())
loop.create_task(main())
loop.run_forever()
