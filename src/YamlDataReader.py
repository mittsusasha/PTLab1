# Новый класс, который заточен на чтение данных из YAML-файлов

# Импорты нужных библиотек и базового класса DataReader
import yaml     # Хорошо, что для чтения YAML-файлов в Python есть специально обученная библиотека с нужным функционалом
from Types import DataType
from DataReader import DataReader


class YamlDataReader(DataReader):  # Наследуем от класса DataReader

    def __init__(self) -> None:           # инициализатор
        # self.key: str = ""              # переменная для хранения ключа тут не подойдёт
        # Почему? Так ведь YAML-файл в образце сделан не просто как словарь, а как список словарей
        self.students: DataType = {}    # словарь для хранения данных студентов

    # Метод для чтения данных формата YAML, основная логика данного класса
    def read(self, path: str) -> DataType:
        # Открываем файл для чтения в кодировке UTF-8 (надеюсь, что там будет UTF-8)
        with open(path, 'r', encoding='utf-8') as file:
            # Загружаем данные из файла в переменную data
            data = yaml.safe_load(file)
            # У препода любимый вопрос — зачем нам нужен обязательно safe_load (а не просто load)
            # Умные дяди с Хабра говорили, что всегда следует использовать yaml.safe_load или yaml.safe_dump
            # Так как YAML может конструировать любой объект Python...
            # ...А это слишком опасно, если мы загружаем файл с помощью yaml.load из ненадёжного источника!
            # см. статью https://habr.com/ru/articles/669684/ в случае необходимости уточнения

            # Пройдём по всем элементам загруженных выше данных (очень удобный синтаксис)
            for student_record in data:
                for key, subjects in student_record.items():
                    # Создаём пустой список, в котором сохраним данные текущего студента
                    self.students[key] = []
                    # И проходим по предметам (subj) и оценкам (score) в записи этого студента
                    for subj, score in subjects.items():
                        # Добавим текущий предмет и оценку в список к остальным студентам
                        self.students[key].append((subj, int(score)))

        # Готово! Возвращаем словарь, в котором будут данные студентов
        return self.students
