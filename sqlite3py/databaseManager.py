import sqlite3

'''
Module sqlite3py provides you smart requests for sqlite database.

Usage:

    >>> import Database

    >>> database = Database('./storage.sqlite', check_same_thread = False)

    # Create table
    >>> database.createTable('files', 'uuid TEXT NOT NULL, path TEXT NOT NULL, creationTime INTEGER NOT NULL')

    # Insert data
    >>> database.insert('files', 'uuid, path, creationTime', '"a8098c1a-f86e-11da-bd1a-00112444be1e", "./image.png"', 1661943437796)
'''

class Database:
    def __init__(self, path: str = 'database.sqlite3', check_same_thread: bool = False):
        self.connection = sqlite3.connect(path, check_same_thread = check_same_thread)
        self.database = self.connection.cursor()

    def createTable(self, nameTable: str, rowsTable: str, existTable: bool = True):
        '''
        Create table of your database.
        * `nameTable: str`, name of create table.
        * `rowsTable: str`, rows of create table.
        * `existTable: bool`, if true used `IF NOT EXISTS`.

        Example usage:

            >>> createTable('users', 'username TEXT NOT NULL, password TEXT')
        '''

        if rowsTable: rowsTable = f'({rowsTable})'
        else: rowsTable = ''

        if existTable: existTable = ' IF NOT EXISTS'
        else: existTable = False

        return self.database.execute(f'CREATE TABLE{existTable} {nameTable}{rowsTable}')



    def removeTable(self, nameTable: str, existTable: bool = True):
        '''
        Remove table from your database.
        * `nameTable: str`, name of create table.
        * `existTable: bool`, if true used `IF EXISTS`.

        Example usage:

            >>> removeTable('users')
        '''

        if existTable: existTable = ' IF EXISTS'
        else: existTable = False

        return self.database.execute(f'DROP TABLE{existTable} {nameTable}')



    def insert(self, nameTable: str, selectRows: str = False, dataRows: str = False):
        '''
        Set data for selected table and row(s).
        * `nameTable: str`, name of table.
        * `selectRows: str`, name of selected row(s) in table.
        * `dataRows: str`, data of selected row(s).

        Example usage:

            >>> insert('users', 'username, password', f'{username}, {password}')
        '''

        if selectRows: selectRows = f'({selectRows})'
        else: selectRows = ''

        if dataRows: dataRows = f' VALUES({dataRows})'
        else: dataRows = ''

        self.database.execute(f'INSERT INTO {nameTable}{selectRows}{dataRows}')
        return self.connection.commit()



    def get(self, nameTable: str, selectRow: str, sqlElements: str = False):
        '''
        Return data from selected table and row.
        * `nameTable: str`, name of table.
        * `selectRows: str`, name of selected row(s) in table,
        * Use `'*'` for all variables.
        * `sqlElements: str`, sql elements like HAVING, WHERE, GROUP_BY and etc..

            >>> sqlElements example: ('WHERE id IN (9722188724768, 5312188724941)')

        Example usage:

            >>> get('users', 'id', 'WHERE name = "Jhon"')
        '''

        if sqlElements: sqlElements = f' {sqlElements}'
        else: sqlElements = ''

        return self.database.execute(f'SELECT {selectRow} FROM {nameTable}{sqlElements}')



    def delete(self, nameTable: str, sqlElements: str = False):
        '''
        Delete data from selected table and row.
        * `nameTable: str`, name of table.
        * `sqlElements: str`, sql elements like HAVING, WHERE, GROUP_BY and etc..

            >>> sqlElements example: ('WHERE id NOT IN (9722188724768, 5312188724941)')

        Example usage:

            >>> delete('users', 'WHERE id = 9722188724768')
        '''

        if sqlElements: sqlElements = f' {sqlElements}'
        else: sqlElements = ''

        self.database.execute(f'DELETE FROM {nameTable}{sqlElements}')
        return self.connection.commit()



    def set(self, nameTable: str, selectRows: str, sqlElements: str = False):
        '''
        Update (Set) data for selected table and row(s).
        * `nameTable: str`, name of table.
        * `selectRows: str`, name of selected row(s) in table.
        * `sqlElements: str`, sql elements like HAVING, WHERE, GROUP_BY and etc..

            >>> sqlElements example: ('ORDER BY name')

        Example usage:

            >>> set('users', 'pass = "root1234"')
        '''

        if sqlElements: sqlElements = f' {sqlElements}'
        else: sqlElements = ''

        self.database.execute(f'UPDATE {nameTable} SET {selectRows}{sqlElements}')
        return self.connection.commit()



    def request(self, request: str, commit: bool = False):
        '''
        Send your SQL request to database.
        * `request: str`, sql request like SELECT, UPDATE, DROP and etc..
        * `commit: bool`, default `False`, send your changes to database.

        Example usage:

            >>> request('DELETE FROM users WHERE id = null')
        '''

        if commit:
            self.database.execute(f'{request}')
            return self.connection.commit()
        else:
            return self.database.execute(f'{request}')