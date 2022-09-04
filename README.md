sqlite3py
=========

Module sqlite3py provides you very easy smart requests for sqlite database.

<div style="width: 100%; display: flex; justify-content: center">
    <img style="text-align: center;" src="https://raw.githubusercontent.com/Xpos587/Sqlite3py/master/sqlite3py.png" alt draggable="false" ></img>
</div>
<a href="https://github.com/Xpos587/Sqlite3py">Read on GitHub</a>
<br>
<a href="https://github.com/Xpos587/Sqlite3py/tree/master/examples">Examples folder</a>

Methods:
--------
- **set** (Update (Set) values for selected row.)
- **insert** (Insert (Push) row.)
- **all** (Return all values.)
- **get** (Return values from selected row.)
- **delete** (Delete selected row.)

#### **Example**

```python
'''After sqlite3py Version 2.0.0'''

from sqlite3py import Database

# Create database 
database = Database('./storage.db', check_same_thread = False)

# Create table
files = database.table('files')

# Set values
files.set('Documentation', {
    'title': 'Documentation',
    'description': 'Some description',
    'type': 'pdf',
    'uuid': 'a8098c1a-f86e-11da-bd1a-00112444be1e',
})

# Get values
files.get('Documentation')[0]['description']
# Return: 'Some description'

# Get all values
files.all()
# Return: [{'key': 'Documentation', 'value': {
#   'title': 'Documentation',
#   'description': 'Some description',
#   'type': 'pdf',
#   'uuid': 'a8098c1a-f86e-11da-bd1a-00112444be1e',
# }}]
```

Requirements Packages
---------------------
- sqlite3 (Already set by default)