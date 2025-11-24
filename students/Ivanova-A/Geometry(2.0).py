import math

while True:
    a = float(input("Введите длину стороны: "))
    n = int(input("Введите количество сторон: "))
    
    perimeter = n * a
    area = (n * a**2) / (4 * math.tan(math.pi / n))
    
    print("Периметр:", perimeter)
    print("Площадь:", area)
    
    answer = input("Хотите выполнить еще один расчет? (да/нет): ")
    if answer.lower() not in ['да', 'д', 'yes', 'y']:
        break
