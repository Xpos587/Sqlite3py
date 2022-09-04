from sqlite3py import Database

database = Database('data.sqlite')

users = database.table('users')

users.set('Jhon', { 'wife': True })

print(users.get('Jhon')[0])