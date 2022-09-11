import sqlite3

def drop_table():
  with sqlite3.connect('items.db') as connection:
    c = connection.cursor()
    c.execute("""DROP TABLE IF EXISTS items;""")
  return True

def create_db():
  with sqlite3.connect('items.db') as connection:
    c = connection.cursor()
    table = """CREATE TABLE items(
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      name TEXT NOT NULL
    );
    """
    c.execute(table)
  return True

def seed_db():
  with sqlite3.connect('items.db') as connection:
    c = connection.cursor()
    names = ["Miles Morales", "Riri Williams", "T'challa"]
    cmd = """INSERT INTO items (name) values(?);"""
    for person in names:
      c.execute("""INSERT INTO items (name) values(?);""", (person,))
  return True

if __name__ == '__main__':
  drop_table()
  create_db()
  seed_db()