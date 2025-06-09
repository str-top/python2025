/*
Создать абстрактный класс фигур (геометрическая фигура), в котором определены две чисто виртуальные функции: 
- вычисление площади;
- вычисление периметра.
 
Создать иерархию классов, которые наследуются от данного класса.
 
Иерархия классов должна включать следующие классы: 
- Triangle (треугольник);
- Circle (круг); 
- Parallelogram (параллелограмм); 
- Rectangle (прямоугольник); 
- Square (квадрат).
 
Разработать программу, в которой множество геометрических фигур сохраняется в виде массива.
Организовать вывод на экран значений периметра и площади для каждой геометрической фигуры.
*/
 
#include <iostream>
#define _USE_MATH_DEFINES
#include <cmath>
 
using namespace std;
 
class Figure { //Базовый, абстрактный класс
 
    public:
 
        //Чисто виртуальные функции базового (абстрактного) класса
 
        virtual void calc_square() const = 0;
        virtual void calc_perimeter() const = 0;
};
 
class Triangle: public Figure { //Класс-потомок (треугольник)
 
    private:
 
        double a, b, c;
 
    public:
 
        //Реализуем виртуальные методы базового (абстрактного) класса
 
        void calc_square() const { //Функция вычисления площади фигуры (треугольника)           
            double p = a + b + c;
            cout << sqrt(p * (p - a) * (p - b) * (p - c));
        }
 
        void calc_perimeter() const { //Функция вычисления периметра фигуры (треугольника)            
            cout << a + b + c;
        }
 
        //Конструктор с параметром (инициализирующий конструктор)
 
        Triangle(double side_a, double side_b, double side_c)
            : a(side_a), b(side_b), c(side_c) {}
};
 
class Circle: public Figure { //Класс-потомок (круг)
 
    private:
 
        double r;
 
    public:
 
        //Реализуем виртуальные методы базового (абстрактного) класса
 
        void calc_square() const { //Функция вычисления площади фигуры (круга)           
            cout << M_PI * r * r;
        }
 
        void calc_perimeter() const { //Функция вычисления периметра фигуры (круга)            
            cout << 2 * M_PI * r;
        }
 
        //Конструктор с параметром (инициализирующий конструктор)
 
        Circle(double radius)
            : r(radius) {}
};
 
class Parallelogram: public Figure { //Класс-потомок (параллелограмм)
 
    private:
 
        double a, b;
        double angle;
 
    public:
 
        //Реализуем виртуальные методы базового (абстрактного) класса
 
        void calc_square() const { //Функция вычисления площади фигуры (параллелограмма)           
            cout << a * b * sin(angle * M_PI / 180);
        }
 
        void calc_perimeter() const { //Функция вычисления периметра фигуры (параллелограмма)            
            cout << 2 * (a + b);
        }
 
        //Конструктор с параметром (инициализирующий конструктор)
 
        Parallelogram(double side_a, double side_b, double alpha)
            : a(side_a), b(side_b), angle(alpha) {}
};
 
class Rectangle: public Figure { //Класс-потомок (прямоугольник)
 
    private:
 
        double a, b;
 
    public:
 
        //Реализуем виртуальные методы базового (абстрактного) класса
 
        void calc_square() const { //Функция вычисления площади фигуры (прямоугольника)           
            cout << a * b;
        }
 
        void calc_perimeter() const { //Функция вычисления периметра фигуры (прямоугольника)            
            cout << 2 * (a + b);
        }
 
        //Конструктор с параметром (инициализирующий конструктор)
 
        Rectangle(double side_a, double side_b)
            : a(side_a), b(side_b) {}
};
 
class Square: public Figure { //Класс-потомок (квадрат)
 
    private:
 
        double a;
 
    public:
 
        //Реализуем виртуальные методы базового (абстрактного) класса
 
        void calc_square() const { //Функция вычисления площади фигуры (квадрата)           
            cout << a * a;
        }
 
        void calc_perimeter() const { //Функция вычисления периметра фигуры (квадрата)            
            cout << 4 * a;
        }
 
        //Конструктор с параметром (инициализирующий конструктор)
 
        Square(double side_a)
            : a(side_a) {}
};
 
int main() {
    Figure** figure = new Figure*[5];
    cout << "Output of the program:\n";
    cout << "\nFigure #1 (triangle):";
    figure[0] = new Triangle(3, 4, 5); //Создаем треугольник со сторонами 3, 4, 5
    cout << "\nSquare: ";
    figure[0]->calc_square(); //Вычисляем площадь треугольника
    cout << "\nPerimeter: ";
    figure[0]->calc_perimeter(); //Вычисляем периметр треугольника
 
    cout << "\n\nFigure #2 (circle):";
    figure[1] = new Circle(5); //Создаем круг с радиусом 5
    cout << "\nSquare: ";
    figure[1]->calc_square(); //Вычисляем площадь круг
    cout << "\nPerimeter: ";
    figure[1]->calc_perimeter(); //Вычисляем периметр круг
 
    cout << "\n\nFigure #3 (parallelogram):";
    figure[2] = new Parallelogram(4, 5, 30); //Создаем параллелограмм со сторонами 4 и 5 и углом 30 градусов
    cout << "\nSquare: ";
    figure[2]->calc_square(); //Вычисляем площадь параллелограмма
    cout << "\nPerimeter: ";
    figure[2]->calc_perimeter(); //Вычисляем периметр параллелограмма
 
    cout << "\n\nFigure #4 (rectangle):";
    figure[3] = new Rectangle(4, 5); //Создаем прямоугольник со сторонами 4 и 5
    cout << "\nSquare: ";
    figure[3]->calc_square(); //Вычисляем площадь прямоугольника
    cout << "\nPerimeter: ";
    figure[3]->calc_perimeter(); //Вычисляем периметр прямоугольника
 
    cout << "\n\nFigure #5 (square):";
    figure[4] = new Square(5); //Создаем квадрат со стороной 5
    cout << "\nSquare: ";
    figure[4]->calc_square(); //Вычисляем площадь квадрата
    cout << "\nPerimeter: ";
    figure[4]->calc_perimeter(); //Вычисляем периметр квадрата
    delete figure[0];
    delete figure[1];
    delete figure[2];
    delete figure[3];
    delete figure[4];
    delete [] figure;
    return 0;
}
