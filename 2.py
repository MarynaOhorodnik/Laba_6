'''
Є описи... x = float (input ( 'amount of money:')), p = converter [input ( 'currency:')]
Значення змінної x, що позначає деяку суму грошей в валюті p, замінити величиною цієї ж суми в гривнях.
'''
while True:
    from enum import Enum
    class converter(Enum):
        USD = 1
        EUR = 2
        CZK = 3
        PLN = 4
    while True:
        try:
            x = float(input('amount of money: '))
            p = converter[input('currency: ')]
            break
        except KeyError:
            print('Currency is incorrect')
        except ValueError:
            print('Amount of money is incorrect')

    if p == converter.USD:
        a = 24.58 * x
        print(f'{x} USD is {round(a, 2)} UAH')
    elif p == converter.EUR:
        b = 26.90 * x
        print(f'{x} EUR is {round(b, 2)} UAH')
    elif p == converter.CZK:
        c = 1.08 * x
        print(f'{x} CZK is {round(c, 2)} UAH')
    elif p == converter.PLN:
        d = 6.31 * x
        print(f'{x} PLN is {round(d, 2)} UAH')

    answer = input('Do you want to run the program again? Yes (+), No (-) ')
    if answer == '+':
        continue
    else:
        break
