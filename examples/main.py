from sqlite3py import Database

database = Database()

database.createTable('people', 'name TEXT NOT NULL, age INTEGER NOT NULL')

database.insert('people', 'name, age', '"Jhon", 24')

print(*database.get('people', '*'))