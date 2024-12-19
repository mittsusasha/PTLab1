import pytest
from Types import DataType
from CalcExcellent import CalcExcellent
from io import StringIO
import sys


class TestCalcExcellent:

    # Фикстура для тестовых данных о студентах и их оценках
    @pytest.fixture()
    def student_data(self) -> DataType:
        # Тестовые данные о студентах и их оценках
        return {
            # Студент номер 1 имеет оценки ниже 90 по русскому языку
            "Студент номер 1": [
                ("математика", 95),
                ("физика", 92),
                ("русский язык", 88)
            ],
            # Студент номер 2 имеет все оценки >= 90 — он отличник
            "Студент номер 2": [
                ("математика", 90),
                ("физика", 91),
                ("английский", 94)
            ],
            # Студент номер 3 также имеет все оценки >= 90 — он отличник
            "Студент номер 3": [
                ("математика", 91),
                ("физика", 92),
                ("программирование", 100)
            ],
            # Студент номер 4 имеет оценки ниже 90 по математике и физике
            "Студент номер 4": [
                ("математика", 85),
                ("физика", 75),
                ("русский язык", 80)
            ]
        }

    # Тест на проверку корректности подсчёта количества студентов-отличников
    def test_calc_with_excellent_students(
        self, student_data: DataType
    ) -> None:
        # Создаем экземпляр класса CalcExcellent с тестовыми данными
        calc = CalcExcellent(student_data)

        # Вызываем метод calc, который должен подсчитать количество отличников
        count = calc.calc()

        # Ожидаем, что отличниками будут только Студенты номер 2 и 3
        # Поэтому ожидаем результат 2
        assert count == 2

    # Не забудем тот момент, что отличников может не оказаться вообще
    def test_calc_without_excellent_students(self) -> None:
        # Изменим данные — пусть все студенты
        student_data = {
            "Студент номер 1": [
                ("математика", 85),
                ("физика", 75),
                ("русский язык", 80)
            ]
        }

        # Создаем экземпляр CalcExcellent с измененными данными
        calc = CalcExcellent(student_data)

        # Вызываем метод calc, который должен подсчитать количество отличников
        count = calc.calc()

        # Ожидаем, что отличников не будет
        assert count == 0

    # Тест на корректность вывода списка отличников
    def test_print_excellent(self, student_data: DataType) -> None:
        calc = CalcExcellent(student_data)
        calc.calc()

        captured_output = StringIO()
        sys.stdout = captured_output  # Перенаправляем вывод в captured_output
        calc.print_excellent()
        sys.stdout = sys.__stdout__  # Восстанавливаем стандартный вывод

        # Проверяем, что в выводе есть информация о количестве отличников
        assert (
            "Количество студентов-отличников: 2"
            in captured_output.getvalue()
        )
        # Проверяем, что в выводе есть информация о нужных намстудентах
        assert "Отличник: Студент номер 2" in captured_output.getvalue()
        assert "Отличник: Студент номер 3" in captured_output.getvalue()

    # Тест на вывод информации об отсутствии студентов-отличников
    def test_print_excellent_no_students(self) -> None:
        # Изменяем данные так, чтобы не было отличников
        student_data = {
            "Студент номер 1": [
                ("математика", 85),
                ("физика", 75),
                ("русский язык", 80)
            ]
        }

        # Создаём экземпляр CalcExcellent и подсчитываем отличников
        calc = CalcExcellent(student_data)
        calc.calc()

        # Захватываем вывод в строковый поток StringIO
        captured_output = StringIO()
        sys.stdout = captured_output  # Перенаправляем вывод в captured_output
        calc.print_excellent()  # Вызываем метод print_excellent
        sys.stdout = sys.__stdout__  # Восстанавливаем стандартный вывод

        # Проверяем, что выводит сообщение о том, что отличников нет
        assert (
            "Студентов-отличников в списке не обнаружено!"
            in captured_output.getvalue()
        )
