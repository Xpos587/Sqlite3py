sqlite3py
=========

Module sqlite3py provides you smart requests for sqlite database.

<div style="width: 100%; display: flex; justify-content: center">
    <img style="text-align: center;" src="./sqlite3py.png" alt></img>
</div>

Methods:
--------
- **createTable** (Create table for your database.)
- **removeTable** (Remove table from your database.)
- **insert** (Insert data for selected table and row(s).)
- **get** (Return data from selected table and row.)
- **delete** (Delete data from selected table and row.)
- **set** (Update (Set) data for selected table and row(s).)
- **request** (Send your SQL request to database.)

#### **Example**

```python
## before:
import sqlite3

connection = sqlite3.connect('database.sqlite3', check_same_thread = False)
cursor = connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS files(uuid TEXT NOT NULL, name TEXT NOT NULL, extension TEXT NOT NULL, description TEXT NOT NULL)''')

description = cursor.execute('''SELECT description FROM files where uuid = ?''', (file,)).fetchone()[0]

cursor.execute('''INSERT INTO files(uuid, name, extension, description) VALUES(?, ?, ?, ?)''', (fileUuid, fileName, fileExtension, fileDescription))

connection.commit()


## after:
import sqlite3py

database = Database()

database.createTable('files', 'uuid TEXT NOT NULL, name TEXT NOT NULL, extension TEXT NOT NULL, description TEXT NOT NULL')

database.get('files', 'description', f'WHERE uuid = "{file}"').fetchone()[0]

database.insert('files', 'uuid, name, extension, description', f'"{fileUuid}", "{fileName}", "{fileExtension}", "{fileDescription}"')
```

Requirements Packages
---------------------
- sqlite3 (Already set by default)