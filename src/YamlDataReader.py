# Новый класс, который заточен на чтение данных из YAML-файлов

# Импорты нужных библиотек и базового класса DataReader
import yaml     # библиотека для работы с YAML-файлами
from Types import DataType
from DataReader import DataReader


class YamlDataReader(DataReader):  # Наследуем от класса DataReader

    def __init__(self) -> None:           # инициализатор
        # self.key: str = ""    # переменная для хранения ключа не подойдёт
        # Почему? Наш YAML-файл не просто как словарь, а как список словарей
        self.students: DataType = {}    # словарь для хранения данных

    # Метод для чтения данных формата YAML, основная логика данного класса
    def read(self, path: str) -> DataType:
        # Открываем файл для чтения в кодировке UTF-8
        with open(path, 'r', encoding='utf-8') as file:
            # Загружаем данные из файла в переменную data
            data = yaml.safe_load(file)
            # У препода любимый вопрос — зачем нам нужен обязательно safe_load
            # Умные дяди с Хабра говорили, что всегда yaml.safe_load
            # Так как YAML может конструировать любой объект Python...
            # ...А это слишком опасно, если читаем из ненадёжного источника!
            # см. статью https://habr.com/ru/articles/669684/

            # Пройдём по всем элементам загруженных выше данных
            for student_record in data:
                for key, subjects in student_record.items():
                    # Создаём пустой список, в него сохраним данные студента
                    self.students[key] = []
                    # И проходим по предметам (subj) и оценкам (score) записи
                    for subj, score in subjects.items():
                        # Добавим текущий предмет и оценку в список
                        self.students[key].append((subj, int(score)))

        # Готово! Возвращаем словарь, в котором будут данные студентов
        return self.students
