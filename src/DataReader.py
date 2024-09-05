# Абстрактный класс, определяющий поведение своих классов-наследников
# реализующих чтение данных из файлов определённых форматов
# -*- coding: utf-8 -*-
from Types import DataType
from abc import ABC, abstractmethod


class DataReader(ABC):

    @abstractmethod
    def read(self, path: str) -> DataType:
        pass
