def get_date():
    while True:
        # assume taking different inputs for each variable
        date, month, year = map(int, input('input date: ').split('/'))
    
        # range check
        if not (0 < date <= 31) or not (0 < month < 12) or year < 0:
            continue
    
        # check if month is any of these
        if month in [4, 6, 9, 11] and date > 30:
            continue
    
        # check if month is feb and not leap year
        if month == 2 and (year % 4 != 0 and year % 400 != 0 or year % 100 == 0):
            # in that case check if date isn't above 28
            if date > 28:
                continue
        else:
            # otherwise check if it isn't above 29
            if date > 29:
                continue
        break
    return date, month, year
    
def calculate_age(birth, current):
    (bdate, bmonth, byear), (cdate, cmonth, cyear) = birth, current
    
    delta_year = cyear - byear
    delta_month = cmonth - bmonth
    delta_date = cdate - bdate

    if delta_year < 0:
        return 'invalid dates'

    if delta_date < 0:
        delta_date += 31
        delta_month -= 1

    if delta_month < 0:
        delta_month += 12
        delta_year -= 1
    
    return f'{delta_year} year(s) {delta_month} month(s) {delta_date} day(s)'

def tests():
    test_cases = [
        [((1, 1, 0), (1, 1, 1)), '1 year(s) 0 month(s) 0 day(s)'],
        [((1, 1, 2), (1, 1, 1)), 'invalid dates'],
        [((6, 7, 2005), (6, 8, 2005)), '0 year(s) 1 month(s) 0 day(s)'],
    ]

    for case, result in test_cases:
        print('test case:', *case)
        value = calculate_age(*case)
        print('result:', value)
        print()
        assert value == result

tests()
