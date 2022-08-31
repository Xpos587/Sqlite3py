from sqlite3py import Database

database = Database()

database.createTable('members', 'name TEXT NOT NULL, number INTEGER NOT NULL')

database.insert('members', 'name, number', '"Max", 25')
database.insert('members', 'name, number', '"Sany", 19')

print(database.get('members', '*').fetchall())

database.set('members', 'number = 20', 'WHERE name = "Sany"')

print(database.get('members', '*').fetchall())

database.delete('members', 'WHERE name = "Max"')

print(database.get('members', '*').fetchall())