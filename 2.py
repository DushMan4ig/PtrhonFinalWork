# Взять любую задачу и настроить в ней запуск скрипта с параметрами. (используем Пайчарм и модуль argparse)
import argparse

def check_triangle(a, b, c):
    # Проверяем условие существования треугольника
    if a + b > c and a + c > b and b + c > a:
        # Треугольник существует

        # Определяем тип треугольника
        if a == b == c:
            return "Треугольник существует\nТреугольник равносторонний"
        elif a == b or b == c or a == c:
            return "Треугольник существует\nТреугольник равнобедренный"
        else:
            return "Треугольник существует\nТреугольник разносторонний"
    else:
        # Треугольник не существует
        return "Треугольник не существует"

def main():
    parser = argparse.ArgumentParser(description="Проверка типа треугольника по длинам его сторон.")
    parser.add_argument("a", type=float, help="Длина первой стороны треугольника")
    parser.add_argument("b", type=float, help="Длина второй стороны треугольника")
    parser.add_argument("c", type=float, help="Длина третьей стороны треугольника")
    
    args = parser.parse_args()
    result = check_triangle(args.a, args.b, args.c)
    print(result)

if __name__ == "__main__":
    main()
