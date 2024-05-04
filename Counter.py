import random
import time


class Counter:
    def __init__(self):
        self.years = 0
        self.months = 0
        self.days = 0
        self.hours = 0
        self.minutes = 0
        self.seconds = 0
        self.isInfinite = False

    def reset_counter(self):
        self.years = 0
        self.months = 0
        self.days = 0
        self.hours = 0
        self.minutes = 0
        self.seconds = 0
        self.isInfinite = False

    def set_counter(self, years, months, days, hours, minutes, seconds):
        self.years = years
        self.months = months
        self.days = days
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_infinite(self, isInfinite):
        self.isInfinite = isInfinite

    def increment_counter(self):
        self.seconds += 1
        if self.seconds == 60:
            self.seconds = 0
            self.minutes += 1
        if self.minutes == 60:
            self.minutes = 0
            self.hours += 1
        if self.hours == 24:
            self.hours = 0
            self.days += 1
        if self.days == 30:
            self.days = 0
            self.months += 1
        if self.months == 12:
            self.months = 0
            self.years += 1

    def decrement_counter(self):
        self.seconds -= 1
        if self.seconds == -1:
            self.seconds = 59
            self.minutes -= 1
        if self.minutes == -1:
            self.minutes = 59
            self.hours -= 1
        if self.hours == -1:
            self.hours = 23
            self.days -= 1
        if self.days == -1:
            self.days = 29
            self.months -= 1
        if self.months == -1:
            self.months = 11
            self.years -= 1

    def countdown(self):
        while True:
            print(
                f"{self.years} years {self.months} months {self.days} days {self.hours} hours {self.minutes} minutes {self.seconds} seconds")
            self.decrement_counter()
            time.sleep(1)

    def set_random_counter(self, time_frame):
        self.reset_counter()

        time_units = {
            "years": 100,
            "months": 12,
            "days": 31,
            "hours": 24,
            "minutes": 60,
            "seconds": 60
        }

        found = False
        for unit, upper_limit in time_units.items():
            if time_frame == unit or found:
                setattr(self, unit, random.randint(0, upper_limit - 1))
                found = True




