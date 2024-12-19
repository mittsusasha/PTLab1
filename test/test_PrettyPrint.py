# -*- coding: utf-8 -*-
import pytest
from io import StringIO  # Импортируем StringIO для захвата вывода в тестах
import sys  # Для перенаправления стандартного вывода
from PrettyPrint import PrettyPrint  # Импортируем класс PrettyPrint


class TestPrettyPrint:

    # Фикстура для предоставления данных о студентах
    @pytest.fixture()
    def students_data(self) -> dict:
        # Словарь, в котором студентам сопоставлены их предметы и оценки
        return {
            "Тестов Тест Тестович": [
                ("математика", 91), ("физика", 90), ("русский язык", 80)
            ],
            "Имяреков Имярек Имярекович": [
                ("математика", 95), ("физика", 98), ("программирование", 100)
            ],
        }

    # Фикстура для предоставления данных о рейтингах студентов
    @pytest.fixture()
    def rating_data(self) -> dict:
        # Словарь, где каждому студенту сопоставлен его рейтинг
        return {
            "Тестов Тест Тестович": 87.0,
            "Имяреков Имярек Имярекович": 97.5,
        }

    # Тест для метода print_students
    def test_print_students(self, students_data):
        # Перенаправляем стандартный вывод в StringIO, чтобы перехватить вывод
        captured_output = StringIO()
        sys.stdout = captured_output

        # Вызываем метод print_students, он выводит информацию на экран
        PrettyPrint.print_students(students_data)

        # Возвращаем стандартный вывод в исходное состояние
        sys.stdout = sys.__stdout__

        # Ожидаемый вывод, который должен совпасть с тем, что будет напечатано
        expected_output = (
            "Сведения об успеваемости студентов:\n\n"
            "Тестов Тест Тестович\n"
            "математика : 91\n"
            "физика : 90\n"
            "русский язык : 80\n\n"
            "Имяреков Имярек Имярекович\n"
            "математика : 95\n"
            "физика : 98\n"
            "программирование : 100\n\n"
        )

        # Проверяем, совпадает ли захваченный вывод с ожидаемым
        assert captured_output.getvalue() == expected_output

    # Тест для метода print_rating
    def test_print_rating(self, rating_data):
        # Перенаправляем стандартный вывод в объект StringIO
        captured_output = StringIO()
        sys.stdout = captured_output

        # Вызываем метод print_rating, он выводит рейтинг студентов
        PrettyPrint.print_rating(rating_data)

        # Возвращаем стандартный вывод в исходное состояние
        sys.stdout = sys.__stdout__

        # Ожидаемый вывод с рейтингами студентов, до 2 знаков после запятой
        expected_output = (
            "Рейтинг студентов:\n\n"
            "Тестов Тест Тестович : 87.00\n"
            "Имяреков Имярек Имярекович : 97.50\n\n"
        )

        # Проверяем, совпадает ли захваченный вывод с ожидаемым
        assert captured_output.getvalue() == expected_output
