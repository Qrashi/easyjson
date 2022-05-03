# easyjson
Load and save json files safely and fast.

Installation:
```shell
pip install easyjson
```

Usage:

```python

from src import easyjson

file = easyjson.open('file.json')  # Load file.json
file.json = {"key": "value"}  # Change values of JSON file.
file2 = easyjson.open('file.json')
# file and file2 are the same!
easyjson.sync()  # Sync all changes to disk
```

Other operations possible:

```python

from src import easyjson

file = easyjson.open('file.json')  # Load file.json
file.save()  # Save the current contents
file.reload()  # Reload the contents from disk
```
