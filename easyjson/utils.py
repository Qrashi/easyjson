"""
Utils for handling JSON files
"""
import json
from os import path, makedirs

from typing import Union, TextIO


def abs_filename(file: str) -> str:
    return path.abspath(file)


def generate(file: str, default: str = "{}") -> bool:
    if not path.exists(file):
        makedirs(path.dirname(file), exist_ok=True)
    file = open(file, "w+")
    file.write(default)
    file.close()
    return False


def check(file: str) -> bool:
    return path.exists(file)


def load(file: str, mode: str = "r", default: str = "{}") -> TextIO:
    generate(file, default)
    return open(file, mode)


class JsonFile:
    """
    A JSON file on the disk
    """

    __filename: str
    json: Union[dict, list]
    __default: str

    def __init__(self, filename: str, default: str = "{}"):
        """
        Create a new json file instance and load data from disk
        :param filename: filename
        :param default: default data to save if file is empty / nonexistent
        """
        self.__filename = filename
        self.__default = default
        self.reload()

    def reload(self):
        """
        Reload from disk
        :return:
        """
        with load(self.__filename, default=self.__default) as file:
            self.json = json.load(file)

    def __save_default(self):
        """
        Save the default data to the disk
        :return:
        """
        with load(self.__filename, mode="w", default=self.__default) as file:
            json.dump(self.__default, file, indent=4, sort_keys=True)
        self.reload()

    def save(self):
        """
        Save the data to the disk
        :return:
        """
        with load(self.__filename, mode="w", default=self.__default) as file:
            json.dump(self.json, file, indent=4, sort_keys=True)
