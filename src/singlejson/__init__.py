"""Load and save json files easily across files."""
from singlejson.fileutils import JSONFile
from singlejson.pool import load, sync
from singlejson.version import __version__

__all__ = ["JSONFile", "load", "sync"]
