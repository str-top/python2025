import math


def pravMnog(a,n):
    perimeter = a * n
    area = (n * a**2) / (4 * math.tan(math.pi / n))
    print("Периметр:", round(perimeter, 2))
    print("Площадь:", round(area, 2))
    
    return{perimeter,area}
    
    
while True:
    a = int(input("Длина стороны: "))
    n = int(input("Количество сторон: "))
    pravMnog(a,n)
    
    cont = int(input('Ееще раз?(0 - нет, остальное - продолжаем)'))
    if cont == 0:
        break
