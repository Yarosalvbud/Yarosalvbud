import asyncio
import time
import random
import os

start_time = time.time()
trains = asyncio.Queue()
stations = []
people_p = []
people_t = []
time_a = []
count_train = 5


class Train:
    def __init__(self, number):
        self.free_place = 400
        self.time_go = {'Рокоссовская': 6, 'Соборная': 3, 'Кристалл': 2, 'Заречная': 7,
                        'Библиотека имени Пушкина': 0}
        self.time_go_b = {'Библиотека имени Пушкина': 7, 'Заречная': 2, 'Кристалл': 3, 'Соборная': 6, 'Рокоссовская': 0}
        self.number = number
        self.current = ''
        self.id = 0
        self.sight = 0

    async def bring_people(self, st):
        people_on_s = st.people
        self.current = st.name
        if self.current == 'Библиотека имени Пушкина':
            self.free_place = 400
            self.sight = 1
            self.id = 0
            print(
                f'Поезд {self.number} высадил всех пассажиров на станции {self.current} и начинает двигаться в обратную сторону')
            print(' ')
        else:
            self.free_place += random.randint(0, 400 - self.free_place) if self.id != 0 else 0
            self.id += 1
            await st.control(self.number, self.free_place)
            self.free_place = 0 if people_on_s > self.free_place else self.free_place - people_on_s
            await asyncio.sleep(0.15)
            print(f'Поезд {self.number} произвёл посадку и высадку пассажиров')
            print(f"Свободных мест в поезде {self.free_place}")
            print(' ')

    async def bring_people_b(self, st):
        people_on_s = st.people_b
        self.current = st.name
        if self.current == 'Рокоссовская':
            self.free_place = 400
            self.sight = 0
            self.id = 0
            print(
                f'Поезд {self.number} высадил всех пассажиров на станции {self.current} и начинает двигаться в обратную сторону')
            print(' ')
        else:
            self.free_place += random.randint(0, 400 - self.free_place) if self.id != 0 else 0
            self.id += 1
            await st.control_b(self.number, self.free_place)
            self.free_place = 0 if people_on_s > self.free_place else self.free_place - people_on_s
            await asyncio.sleep(0.15)
            print(f'Поезд {self.number} произвёл посадку и высадку пассажиров')
            print(f"Свободных мест в поезде {self.free_place}")
            print(' ')

    async def train_go(self, st):
        print('Поезд движется на следующую станцию')
        if self.sight == 0:
            await self.bring_people(st)
            await asyncio.sleep(self.time_go.get(st.name))
        else:
            await self.bring_people_b(st)
            await asyncio.sleep(self.time_go_b.get(st.name))


class Station:

    def __init__(self, name):
        self.name = name
        self.people = 0
        self.people_b = 0

    async def control(self, number, free_place):
        print(f"Поезд {number} прибыл на станцию {self.name}")
        print(f"Людей на станци {self.name} {self.people}")
        self.people = self.people - free_place if self.people > free_place else 0
        print(f"Людей на станци {self.name} {self.people}")

    async def control_b(self, number, free_place):
        print(f"Поезд {number} прибыл на станцию {self.name}")
        print(f"Людей на станци {self.name}--{self.people_b}")
        self.people_b = self.people_b - free_place if self.people_b > free_place else 0
        print(f"Людей на станци {self.name}--{self.people_b}")

    async def passengers(self):
        while True:
            if time.time() - start_time >= 18:
                coin = random.randint(0, 1)
                if coin == 0 and self.name != 'Библиотека имени Пушкина':
                    self.people += 1
                elif coin == 0 and self.name == 'Библиотека имени Пушкина':
                    self.people_b += 1
                elif self.name != 'Рокоссовская' and coin == 1:
                    self.people_b += 1
                elif self.name == 'Рокоссовская' and coin == 1:
                    self.people += 1
                await asyncio.sleep(0.016)
            else:
                await asyncio.sleep(18)


async def trains_online():
    num = 0
    for i in range(count_train):
        num += 1
        train = Train(num)
        await trains.put(train)
        await asyncio.sleep(38 / count_train)


async def main():
    while True:
        train = await trains.get()
        st = stations[train.id] if train.sight == 0 else stations_b[train.id]
        await train.train_go(st)
        await trains.put(train)


async def get_average(people_p, people_t):
    pass


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
stations_b = stations[::-1]

loop = asyncio.get_event_loop()
loop.create_task(Rok.passengers())
loop.create_task(Sob.passengers())
loop.create_task(Cry.passengers())
loop.create_task(Zar.passengers())
loop.create_task(Lib.passengers())
loop.create_task(trains_online())
for i in range(count_train):
    loop.create_task(main())
loop.run_forever()
