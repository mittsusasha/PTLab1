# Основная функция программы и вспомогательные функции
# -*- coding: utf-8 -*-
import argparse
import sys

from CalcRating import CalcRating
from YamlDataReader import YamlDataReader
# from TextDataReader import TextDataReader     # Больше не нужно
from CalcExcellent import CalcExcellent
from PrettyPrint import PrettyPrint  # Для читаемости вывода


def get_path_from_arguments(args) -> str:
    parser = argparse.ArgumentParser(description="Path to datafile")
    parser.add_argument(
        "-p", dest="path", type=str, required=True, help="Path to datafile"
    )
    args = parser.parse_args(args)
    return args.path


def main():
    path = get_path_from_arguments(sys.argv[1:])

    # Раньше было reader = TextDataReader() — но теперь мы читаем YAML!
    reader = YamlDataReader()
    students = reader.read(path)
    PrettyPrint.print_students(students)

    rating = CalcRating(students).calc()
    PrettyPrint.print_rating(rating)

    # Создаем объект для подсчета студентов-отличников
    excellent_calc = CalcExcellent(students)

    # Подсчитываем количество студентов-отличников
    excellent_calc.calc()

    # Выводим информацию о отличниках
    excellent_calc.print_excellent()


if __name__ == "__main__":
    main()
