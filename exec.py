import datetime


def week_number_of_month(date_value):
    return (date_value.isocalendar()[1] - date_value.replace(day=1).isocalendar()[1] + 1)


def dates_test():
    today = datetime.datetime.now()
    print(today)
    # print(round(datetime.datetime.now().timestamp()))
    print(today.strftime("%B"))  # month name
    # print(datetime.date.isocalendar())
    print(week_number_of_month(today))


if __name__ == '__main__':
    # dates_test()
    date1 = datetime.datetime.fromisoformat("2022-01-01 00:00:00")
    print(date1.timestamp())
    print(datetime.datetime.fromtimestamp(1640988000.0).__eq__(date1))
