import sqlite3

'''
Module sqlite3py provides you very easy smart requests for sqlite database.

Usage:

    >>> from sqlite3py import Database

    >>> database = Database('./storage.db', check_same_thread = False)

    # Create table
    >>> users = database.table('users')
    # Return: None

    # Remove table
    >>> users.remove()
    # Return: None

    # Insert row
    >>> database.insert('Jhon', { 'wife': False })
    # Return: None

    # Set value
    >>> database.set('Jhon', { 'wife': True })
    # Return: None

    # Get all values
    >>> database.all()
    # Return: [
    # {'key': 'Jhon', 'value': { 'wife': True }}
    # ]

    # Get values
    >>> database.get('Jhon')[0]['wife']
    # Return: True

    >>> database.get('Jhon')[0]
    # Return: { 'wife': True }

    # Delete row
    >>> database.delete('Jhon')
    # Return: None
'''

class Database:
    def __init__(self, path: str = 'database.sqlite3', check_same_thread: bool = False, *args):
        self.connection = sqlite3.connect(path, check_same_thread = check_same_thread, *args)
        self.database = self.connection.cursor()

        self.database.execute(f'CREATE TABLE IF NOT EXISTS data(Key TEXT, Value TEXT)')

    def all(self):
        '''
        Return all rows from database.

        Example usage:

            >>> database.all()
            # Return: [
            # {'key': 'Michael', 'value': { 'age': 15 }},
            # {'key': 'Sany', 'value': { 'age': 24, 'have_car': True }}]
        '''

        rows = self.database.execute(f'SELECT * FROM data')

        table = []

        for row in rows.fetchall():

            key = row[0]
            try: value = eval(row[1])
            except NameError as err:
                value = str(row[1])

            table.append({
                    'key': key,
                    'value': value
                })

        if table: return table
        else: return False



    def get(self, select: str):
        '''
        Return selected row values from database.
        * `select: str`, Key of selected row.

        Example usage:

            >>> database.get('Michael')
            # Return: { 'age': 15 }
        '''
        
        res = []

        if self.all():
            for object in self.all():
                if object['key'] == select:
                    res.append(object['value'])
                continue
        else: return False

        if res: return res
        else: return False



    def set(self, select: str, value, createIfNotExist: bool = True):
        '''
        Update (Set) value for selected row.
        * `select: str`, Key of selected row.
        * `value`, Key value.
        * `createIfNotExist: bool = True`, Create row, if selected row not exist.

        Example usage:

            >>> database.set('Michael', { 'age': 16 })
            # Return: None
        '''

        if self.get(select) is False:
            if createIfNotExist:
                self.insert(select, value)
            else: return

        self.database.execute(f'UPDATE data SET Value = "{value}" WHERE Key = "{select}"')
        return self.connection.commit()



    def insert(self, select: str, value, dontInsertIfExist: bool = False):
        '''
        Insert (Push) row.
        * `select: str`, Key of selected row.
        * `value`, Key value.
        * `dontInsertIfExist: bool = False`, Don't insert, if selected row exist.

        Example usage:

            >>> database.insert('Georgi', { 'age': 29, 'have_car': False }, True)
            # Return: None
        '''

        if self.get(select):
            if dontInsertIfExist: return

        self.database.execute(f'INSERT INTO data(Key, Value) VALUES("{select}", "{value}")')
        return self.connection.commit()



    def delete(self, select: str):
        '''
        Delete row.
        * `select: str`, Key of selected row.

        Example usage:

            >>> database.delete('Georgi')
            # Return: None
        '''

        self.database.execute(f'DELETE FROM data WHERE Key = "{select}"')
        return self.connection.commit()



    def table(self, nameTable: str):
        '''
        Class Table (Create table if not exist).
        * `nameTable: str`, Name of table.

        Example usage:

            >>> users = database.table('users')
            # Return: None
        '''

        return Table(self.connection, self.database, nameTable)


class Table:
    '''
    Class Table (Create table if not exist).
    * `nameTable: str`, Name of table.

    Example usage:

        >>> users = database.table('users')
        # Return: None
    '''

    def __init__(self, connection, database, nameTable: str):
        self.connection = connection
        self.database = database
        self.nameTable = nameTable

        database.execute(f'CREATE TABLE IF NOT EXISTS {nameTable}(Key TEXT, Value TEXT)')



    def remove(self, existTable: bool = True):
        '''
        Remove table.
        * `existTable: bool = True`, Remove table if exist.

        Example usage:

            >>> database.table('users').remove()
            # Return: None
        '''

        if existTable: existTable = ' IF EXISTS'
        else: existTable = ''

        return self.database.execute(f'DROP TABLE{existTable} {self.nameTable}')



    def all(self):
        '''
        Return all rows from table.

        Example usage:

            >>> database.table('users').all()
            # Return: [
            # {'key': 'Michael', 'value': { 'age': 15 }},
            # {'key': 'Sany', 'value': { 'age': 24, 'have_car': True }}]
        '''

        rows = self.database.execute(f'SELECT * FROM {self.nameTable}')

        table = []

        for row in rows.fetchall():

            key = row[0]
            try: value = eval(row[1])
            except NameError as err:
                value = str(row[1])

            table.append({
                    'key': key,
                    'value': value
                })

        if table: return table
        else: return False



    def get(self, select: str):
        '''
        Return selected row values from table.
        * `select: str`, Key of selected row.

        Example usage:

            >>> database.table('users').get('Michael')
            # Return: { 'age': 15 }
        '''
        
        res = []

        if self.all():
            for object in self.all():
                if object['key'] == select:
                    res.append(object['value'])
                continue
        else: return False

        if res: return res
        else: return False



    def set(self, select: str, value, createIfNotExist: bool = True):
        '''
        Update (Set) value for selected row.
        * `select: str`, Key of selected row.
        * `value`, Key value.
        * `createIfNotExist: bool = True`, Create row, if selected row not exist.

        Example usage:

            >>> database.table('users').set('Michael', { 'age': 16 })
            # Return: None
        '''

        if self.get(select) is False:
            if createIfNotExist:
                self.insert(select, value)
            else: return

        self.database.execute(f'UPDATE {self.nameTable} SET Value = "{value}" WHERE Key = "{select}"')
        return self.connection.commit()



    def insert(self, select: str, value, dontInsertIfExist: bool = False):
        '''
        Insert (Push) row.
        * `select: str`, Key of selected row.
        * `value`, Key value.
        * `dontInsertIfExist: bool = False`, Don't insert, if selected row exist.

        Example usage:

            >>> database.table('users').insert('Georgi', { 'age': 29, 'have_car': False }, True)
            # Return: None
        '''

        if self.get(select):
            if dontInsertIfExist: return

        self.database.execute(f'INSERT INTO {self.nameTable}(Key, Value) VALUES("{select}", "{value}")')
        return self.connection.commit()



    def delete(self, select: str):
        '''
        Delete row.
        * `select: str`, Key of selected row.

        Example usage:

            >>> database.table('users').delete('Georgi')
            # Return: None
        '''

        self.database.execute(f'DELETE FROM {self.nameTable} WHERE Key = "{select}"')
        return self.connection.commit()