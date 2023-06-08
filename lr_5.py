#Создайте итерируемый объект, возвращающий генератор тридцати пяти чисел трибоначчи и выведите эти числа.
import self as self


class tribRec1:
    def __init__(self, length):
        self.sequence = []
        self.length = length

    def __iter__(self):
        n = 0

        while n <= self.length:
            if n <= 2:
                if n == 2:
                    t = 1
                    self.sequence.append(t)
                else:
                    t = 0
                    self.sequence.append(t)
            else:
                t = self.sequence[n-1] + self.sequence[n-2] + self.sequence[n-3]
                self.sequence.append(t)
            n += 1
            yield t


if __name__ == '__main__':
    iterator = tribRec1(35)
    for i in iterator:
        print(i)

#Добавьте 5 магических метода к классу из предыдущего ДЗ\
# __init__
# __str__
# __getattr__
# __setattr__
# __len__


from calendar import weekday
from datetime import time
from typing import Any

import datetime


class Airline:
    __days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sut', 'Sun']
    flights = []
    canceledFlightsCount = 0

    def __init__(self, destination, flightNo, airlineType, flightTime, flightDay):
        if Airline.is_valid_day(flightDay) and Airline.is_valid_string(destination):
            self.__destination = destination
            self.__flightNo = flightNo
            self.__airlineType = airlineType
            self.__flightTime = flightTime
            self.__flightDay = flightDay
            self.flights.append(self)

    def __str__(self):
        return self.__destination + ' ' + self.__flightNo + ' ' + self.__airlineType + ' ' + self.__flightDay + ' ' + self.__flightTime

    def __getattr__(self, attr):
        if attr == 'destination':
            return self.__destination
        elif attr == 'flightNo':
            return self.__flightNo
        elif attr == 'airlineType':
            return self.__airlineType
        elif attr == 'flightTime':
            return self.__flightTime
        elif attr == 'flightDay':
            return self.__flightDay
        elif attr == 'flightTime':
            return self.__flightTime

    def set_destination(self, destination):
        if Airline.is_valid_string(destination):
            self.__destination = destination

    def set_flightNo(self, flightNo):
        if Airline.is_valid_string(flightNo):
            self.__destination = flightNo

    def set_airlineType(self, airlineType):
        if Airline.is_valid_string(airlineType):
            self.__airlineType = airlineType

    def set_flightDay(self, flightDay):
        if Airline.is_valid_day(flightDay):
            self.__flightDay = flightDay

    def __setattr__(self, attrname, value):
        self.__dict__[attrname] = value

    def __len__(self):
        return len(self.flights)

    @staticmethod
    def is_valid_string(val):
        try:
            str_value = str(val)
            is_valid = len(str_value) > 0
            if not is_valid:
                print('Empty fields are not allowed')
            return is_valid
        except:
            print('String is invalid')
            return False

    @staticmethod
    def is_valid_day(val):
        try:
            is_valid = val in Airline.__days
            if not is_valid:
                print('Day is invalid. Possible values: Mon, Tue, Wed, Thu, Fri, Sut, Sun')
            return is_valid
        except:
            print('Day is invalid')
            return False

    def flight_of_day(day):
        for i in range(len(Airline.flights)):
            if Airline.flights[i].flightDay == day:
                print(Airline.flights[i])

    def flight_of_destination(destination):
        for i in range(len(Airline.flights)):
            if Airline.flights[i].destination ==destination:
                print(Airline.flights[i])

flight_1 = Airline('Barselona', '1A', 'vip', '10:30', 'Mon')
flight_1.set_flightNo('ABC')
flight_2 = Airline('Madrid', '2B', 'business', '15:00', 'Mon')
flight_3 = Airline('Barselona', '1A', 'vip', '10:30', 'Tue')
flight_4 = Airline('Barselona', '3A', 'vip', '00:30', 'Wed')

Airline.flight_of_day('Mon')
Airline.flight_of_destination('Barselona')

print(Airline.__len__())

