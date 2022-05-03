"""
A package for easily maintaining JSON files

open a JSON file using open()
if you call open with the same filename again, the same object will be returned.
sync all changes to disk using sync()
"""
from typing import List

import utils as __jsonutils

__file_pool: List[__jsonutils.JsonFile] = {}


def open(filename: str, default: str = "{}") -> __jsonutils.JsonFile:
    """
    Open a JsonFile (synchronously)
    :param filename: Path to JSON file on disk
    :param default: Default file contents to save if file is nonexistent
    :return: the corresponding JsonFile
    """
    filename = __jsonutils.abs_filename(filename)
    if filename not in __file_pool:
        __file_pool[filename] = __jsonutils.JsonFile(filename, default=default)
    return __file_pool[filename]


def sync():
    """
    Sync changes to the filesystem
    :return:
    """
    for file in __file_pool:
        file.save()
