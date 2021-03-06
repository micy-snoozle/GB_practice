# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

# Занчения аргументов задавала в PyCharm > Modify Run Configuration > Parameters
from sys import argv

employee, production, rate, premium = argv

result = (int(production) * int(rate)) + int(premium)
print(f'Ваша заработная плата равна: {result}')


# правильный вариант решения (после разбора на уроке)

def salary():
    try:
        time, rate, bonus = map(float, argv[1:])
        print(f'salary - {time * rate + bonus}')
    except ValueError:
        print('enter aal 3 numbers. not string or empty character.')

salary()