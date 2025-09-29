import math

def calculate_polygon(side_length, sides_count):
    perimeter = side_length * sides_count
    
    area = (sides_count * side_length ** 2) / (4 * math.tan(math.pi / sides_count))
    
    return perimeter, area

def main():
    try:
        side_length = float(input("Введите длину стороны многоугольника: "))
        sides_count = int(input("Введите количество сторон: "))
        
        if side_length <= 0 or sides_count < 3:
            print("Длина стороны должна быть положительным числом, а количество сторон — целым числом не меньше 3.")
            return
        
        perimeter, area = calculate_polygon(side_length, sides_count)
        
        print(f"\nПериметр правильного многоугольника: {perimeter:.2f}")
        print(f"Площадь правильного многоугольника: {area:.2f}")
        
    except ValueError:
        print("Пожалуйста, введите корректные числовые значения.")

if __name__ == "__main__":
    main()
