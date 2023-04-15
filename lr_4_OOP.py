# Kласс Airline: Пункт назначения, Номер рейса, Тип самолета, Время вылета, Дни недели.
# Функции- члены реализуют запись и считывание полей (проверка корректности).
# Создать список объектов. Вывести:
# a)	список рейсов для заданного пункта назначения;
# б) список рейсов для заданного дня недели;.
from calendar import weekday
from datetime import time
from typing import Any

import datetime


class Airline:
    __days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sut', 'Sun']
    flights = []

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

    def get_destination(self):
        return self.__destination

    def get_flightNo(self):
        return self.__flightNo

    def get_airlineType(self):
        return self.__airlineType

    def get_flightTime(self):
        return self.__flightTime

    def get_flightDay(self):
        return self.__flightDay

    def set_destination(self, destination):
        if Airline.is_valid_string(destination):
            self.__destination = destination

    def set_flightNo(self, flightNo):
        if Airline.is_valid_string(flightNo):
            self.__flightNo = flightNo

    def set_airlineType(self, airlineType):
        if Airline.is_valid_string(airlineType):
            self.__airlineType = airlineType

    def get_flightTime(self):
        return self.__flightTime

    def set_flightDay(self, flightDay):
        if Airline.is_valid_day(flightDay):
            self.__flightDay = flightDay

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
            if Airline.flights[i].get_flightDay() == day:
                print(Airline.flights[i])

    def flight_of_destination(destination):
        for i in range(len(Airline.flights)):
            if Airline.flights[i].get_destination() == destination:
                print(Airline.flights[i])

flight_1 = Airline('Barselona', '1A', 'vip', '10:30', 'Mon')
flight_1.set_flightNo('1ABC')
flight_2 = Airline('Madrid', '2B', 'business', '15:00', 'Mon')
flight_3 = Airline('Barselona', '1A', 'vip', '10:30', 'Tue')
flight_3 = Airline('Barselona', '3A', 'vip', '00:30', 'Wed')

Airline.flight_of_day('Mon')
Airline.flight_of_destination('Barselona')
