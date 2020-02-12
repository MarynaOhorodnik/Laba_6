'''
Робота світлофора для водіїв запрограмована таким чином: на початку кожної години протягом трьох хвилин горить
зелений сигнал, потім протягом однієї хвилини - жовтий, протягом двох хвилин - червоний, протягом трьох хвилин -
знову зелений і т. д. Розробити програму, яка вводить дійсне число t, що означає час в хвилинах, що минув з початку
чергової години і визначає сигнал якого кольору горить для водіїв в цей момент.
'''
while True:
    while True:
        try:
            x = int(input('Input minutes: '))
            break
        except ValueError or NameError:
            print('Error')

    if x in range(1, 60):
        if x in range(1, 60, 6) or x in range(2, 60, 6) or x in range(3, 60, 6):
            print(f'Traffic lights is green.')
        elif x in range(4, 60, 6):
            print(f'Traffic lights is yellow.')
        elif x in range(5, 60, 6) or x in range(6, 60, 6):
            print(f'Traffic lights is red.')
    else:
        print('You can choose only from 1 to 59 minutes.')

    answer = input('Do you want to run the program again? Yes (+), No (-) ')
    if answer == '+':
        continue
    else:
        break
