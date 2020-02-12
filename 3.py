'''
Є описи... s = month [input ( 'month:')]. За s-назвою місяця визначити відповідну пору року.
'''
while True:
    from enum import Enum
    class month(Enum):
        January = 1
        February = 2
        March = 3
        April = 4
        May = 5
        June = 6
        July = 7
        August = 8
        September = 9
        October = 10
        November = 11
        December = 12
    class season(Enum):
        Winter = 1
        Spring = 2
        Summer = 3
        Autumn = 4
    while True:
        try:
            s = month[input('month: ')]
            break
        except KeyError:
            print('Error')
        except ValueError:
            print('Error')

    if s == month(12) or s == month(1) or s == month(2):
        k = 1
    elif s == month(3) or s == month(4) or s == month(5):
        k = 2
    elif s == month(6) or s == month(7) or s == month(8):
        k = 3
    else:
        k = 4
    print(f'It is {(season(k))}.')

    answer = input('Do you want to run the program again? Yes (+), No (-) ')
    if answer == '+':
        continue
    else:
        break
