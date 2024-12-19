# Класс, с помощью которого осуществляется тестирование класса YamlDataReader
import pytest
import yaml
from Types import DataType
from YamlDataReader import YamlDataReader


class TestYamlDataReader:

    @pytest.fixture()
    def file_and_data_content(self) -> tuple[str, DataType]:
        # Тестовые данные в виде формата YAML для проверки результата
        yaml_text = """
        - Тестов Тест Тестович:
            математика: 91
            физика: 90
            русский язык: 80
        - Имяреков Имярек Имярекович:
            математика: 95
            физика: 98
            программирование: 100
        """

        # Ожидаемый результат — пусть метод read вернёт такой словарь
        data = {
            "Тестов Тест Тестович": [
                ("математика", 91), ("физика", 90), ("русский язык", 80)
            ],
            "Имяреков Имярек Имярекович": [
                ("математика", 95), ("физика", 98), ("программирование", 100)
            ],
        }
        return yaml_text, data

    @pytest.fixture()
    def yaml_filepath_and_data(
        self, file_and_data_content: tuple[str, DataType], tmpdir
    ) -> tuple[str, DataType]:
        # Создадим наш тестовый YAML-файл в директории tmpdir
        p = tmpdir.mkdir("datadir").join("my_data.yaml")
        # И запишем содержимое этого файла в кодировке UTF-8
        p.write_text(file_and_data_content[0], encoding="utf-8")
        # Вернём путь к нашему файлу и ожидаемые данные
        return str(p), file_and_data_content[1]

    def test_read_yaml_file(
            self, yaml_filepath_and_data: tuple[str, DataType]
    ) -> None:
        # Создадим экземляр YamlDataReader и его методом read прочтём данные
        file_content = YamlDataReader().read(yaml_filepath_and_data[0])
        # Проверяем, соответствуют ли они ожидаемым
        assert file_content == yaml_filepath_and_data[1]
