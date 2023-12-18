def calculate_fuel_percentage(fuel_fraction):
    try:
        x, y = map(int, fuel_fraction.split('/'))
        if x <= 0 or y <= 0 or x > y:
            raise ValueError('Invalid fraction')
        percentage = (x / y) * 100
        if percentage <= 1:
            return 'E'  # пустой бак
        elif percentage >= 99:
            return 'F'  # полный бак
        else:
            return str(round(percentage)) + '%'
    except ValueError:
        print('Введите дробь в формате x/y, где x и y - целые положительные числа, x <= y')
    except ZeroDivisionError:
        print('Знаменатель не должен быть равен нулю')

def main():
    while True:
        fuel_fraction = input("Дробь: ")
        percentage = calculate_fuel_percentage(fuel_fraction)
        if percentage:
            print(percentage)
            break

if __name__ == '__main__':
    main()
