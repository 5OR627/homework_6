import time as t
from itertools import cycle


"""Задача 1"""


class TrafficLight:
    lights_order = ('Красный', 'Желтый', 'Зеленый')
    work_time = (7, 2, 5)

    def __init__(self, color):
        self.__color = color

    def color_change(self):
        work = cycle(self.lights_order)
        for light in work:
            if self.__color == light:
                print(f'Загорелся {light} свет')
                t.sleep(self.work_time[self.lights_order.index(light)])
                self.__color = next(work)


item = TrafficLight('Красный')
item.color_change()


"""Задача 2"""


class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass_count(self):
        m = self._length * self._width * 25 * 0.05
        return m


area_1 = Road(7000, 10)
print(area_1.mass_count())


"""Задача 3"""


class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


position_1 = Position('Alexander', 'Egorov', 'engineer', 100000, 10000)
print(f'{position_1.get_full_name()} gets {position_1.get_total_income()}')


"""Задача 4"""


class Car:
    def __init__(self, speed, color, name, is_police=bool):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} starts')

    def stop(self):
        print(f'{self.name} stops')

    def turn(self, direction):
        print(f'{self.name} turns {direction}')

    def show_speed(self):
        print(f'Current speed of {self.name} is {self.speed}')


class TownCar(Car):

    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print('Speed limit is exceeded')


class SportCar(Car):

    def ride(self):
        print('Ride sportcar')


class WorkCar(Car):

    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print('Speed limit is exceeded')


class PoliceCar(Car):

    def pursue(self):
        print('Chasing criminal')


car_1 = TownCar(90, 'blue', 'toyota', False)
car_2 = SportCar(180, 'red', 'ferrari', False)
car_3 = WorkCar(40, 'white', 'kamaz', False)
car_4 = PoliceCar(120, 'black', 'ford', True)

car_3.go()
car_1.show_speed()
car_4.pursue()
car_3.stop()


"""Задача 5"""


class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'{self.title} draws')


class Pen(Stationary):
    def draw(self):
        print(f'You take {self.title}')
        super().draw()


class Pencil(Stationary):
    def draw(self):
        print(f'You take {self.title}')
        super().draw()


class Marker(Stationary):
    def draw(self):
        print(f'You take {self.title}')
        super().draw()


s_1 = Pen('pen')
s_2 = Pencil('pencil')
s_3 = Marker('marker')

s_1.draw()
s_2.draw()
s_3.draw()
