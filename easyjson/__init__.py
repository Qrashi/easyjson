"""
A package for easily maintaining JSON files

open a JSON file using open()
if you call open with the same filename again, the same object will be returned.
sync all changes to disk using sync()
"""
from typing import List

import jsonutils

_file_pool: List[jsonutils.JsonFile] = {}


def open(filename: str, default: str = "{}") -> jsonutils.JsonFile:
    """
    Open a JsonFile (synchronously)
    :param filename: Path to JSON file on disk
    :param default: Default file contents to save if file is nonexistent
    :return: the corresponding JsonFile
    """
    filename = jsonutils.abs_filename(filename)
    if filename not in _file_pool:
        _file_pool[filename] = jsonutils.JsonFile(filename, default=default)
    return _file_pool[filename]


def sync():
    """
    Sync changes to the filesystem
    :return:
    """
    for file in _file_pool:
        file.save()
