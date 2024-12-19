from Types import DataType

# Этот класс вычисляет данные, относящиеся к студентам-отличникам


class CalcExcellent:
    def __init__(self, data: DataType) -> None:
        # конструктор класса, инициализирует данные и список отличников
        self.data: DataType = data  # сохраняем переданные данные о студентах
        self.excellent_students: list = []  # вот в этот список

    def calc(self) -> int:
        # Метод для подсчета количества студентов-отличников
        for student_name, subjects in self.data.items():
            # Проходим по каждой оценке каждого студента
            # Оценок менее 90 баллов у отличника быть не должно
            if all(subject[1] >= 90 for subject in subjects):
                # Если все оценки >= 90, добавим студента в список отличников
                self.excellent_students.append((student_name, subjects))

        # Возвращаем количество студентов-отличников
        return len(self.excellent_students)

    def print_excellent(self) -> None:
        # Выводим количество студентов, которые стали отличниками
        print(
            f"Количество студентов-отличников: {len(self.excellent_students)}")
        # Оригинально и неизбито — просто выведем длину списка!

        # Если в списке есть студенты-отличники — выводим их данные
        if self.excellent_students:
            print("\nСписок студентов-отличников:")
            for student_name, subjects in self.excellent_students:
                # Выводим имя студента
                print(f"\nОтличник: {student_name}")
                print("Оценки:")
                # Проходим по предметам и выводим оценку для каждого
                for subject, grade in subjects:
                    print(f"  {subject}: {grade}")
        else:
            # Но вообще-то, отличников может не быть вовсе...
            print("Студентов-отличников в списке не обнаружено!")
