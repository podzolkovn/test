class Date:
    def __init__(self, year: int, month: int, day: int) -> str:

        self.year = year
        self.month = month
        self.day = day

        self.validation()

    @staticmethod
    def validation_int(name: str, value, min_int: int, max_int: int) -> None:
        if str(value).isalpha():
            raise DateTimeErrorException(name, value, 'an integer')
        elif min_int <= int(value) <= max_int:
            pass
        else:
            raise DateTimeErrorException(name, value, f'between {min_int} and {max_int}')

    @staticmethod
    def validate_day(year: int, month: int, day: int):
        if not str(day).isalpha():
            if month == 2:
                max_day = 29 if (int(year) % 4 == 0 and int(year) % 100 != 0) or int(year) % 400 == 0 else 28
            elif month in (4, 6, 9, 11):
                max_day = 30
            else:
                max_day = 31

            if 1 <= int(day) <= max_day:
                return
            raise DateTimeErrorException('day', day, f'between 1 and {max_day}')
        else:
            raise DateTimeErrorException('day', day, 'an integer')

    def validation(self):
        self.validation_int(name='year', value=self.year, min_int=1, max_int=9999)
        self.validation_int('month', self.month, 1, 12)
        self.validate_day(self.year, self.month, self.day)

    def __str__(self):
        return f'{int(self.year):04d}/{int(self.month):02d}/{int(self.day):02d}'


class DateTime(Date):
    def __init__(self, year: int, month: int, day: int, hour: int, minute: int, second: int) -> str:
        super().__init__(year, month, day)
        self.hour = hour
        self.minute = minute
        self.second = second

        self.validation_datetime()

    def validation_datetime(self):
        self.validation_int('hour', self.hour, 0, 23)
        self.validation_int('minute', self.minute, 0, 59)
        self.validation_int('second', self.second, 0, 59)

    def __str__(self):
        return f'{super().__str__()} {int(self.hour):02d}:{int(self.minute):02d}:{int(self.second):02d}'


class DateTimeErrorException(Exception):
    def __init__(self, name, value, message, *args, **kwargs):
        super().__init__(args, kwargs)
        self.name = name
        self.value = value
        self.message = message

    def __str__(self):
        return f'Invalid value: "{self.value}" for {self.name}. It should be {self.message}'


try:
    date = Date(0, 11, '5')
    print(date)
except DateTimeErrorException as e:
    print(e)

try:
    datetime = DateTime('2100', 2, 29, 0, 4, 6)
    print(datetime)
except DateTimeErrorException as e:
    print(e)

try:
    datetime = DateTime('2026', 4, 31, 0, 4, 6)
    print(datetime)
except DateTimeErrorException as e:
    print(e)

try:
    datetime = DateTime(1568, 2, 29, 0, 4, 6)
    print(datetime)
except DateTimeErrorException as e:
    print(e)

try:
    datetime = DateTime('efw', 2, 29, 0, 4, 6)
    print(datetime)
except DateTimeErrorException as e:
    print(e)

try:
    datetime = DateTime(2321, 1, 15, 24, 4, 6)
    print(datetime)
except DateTimeErrorException as e:
    print(e)

try:
    datetime = DateTime(2321, 1, 15, 15, 'bhvuyt', 6)
    print(datetime)
except DateTimeErrorException as e:
    print(e)

try:
    datetime = DateTime(2321, 1, 15, 17, 4, 0)
    print(datetime)
except DateTimeErrorException as e:
    print(e)
