
# Usando SQLite3
# https://www.digitalocean.com/community/tutorials/how-to-use-the-sqlite3-module-in-python-3

"""STEP 2 - Creazione database SQLite."""
import sqlite3
from contextlib import closing

# .connect viene usatop per connettermi al file database .db. Se il file non esiste, lo crea.
connection = sqlite3.connect('acquarium.db')

# connection.total_changes e' il numero totale di righe del database che sono state cambiate da connection.
# Nel nostro caso stampa 0 perche' non ha cambiato alcuna riga.

print(connection.total_changes)

"""STEP 2 - Aggiungere dati al database SQLite."""

cursor = connection.cursor()

# cursor.execute("CREATE TABLE fish(name TEXT, species TEXT, tank_number INTEGER)")
cursor.execute("INSERT INTO fish VALUES ('Sammy', 'shark', 1)")
cursor.execute("INSERT INTO fish VALUES ('Jamie', 'cuttlefish', 7)")
cursor.execute("INSERT INTO fish VALUES ('Sandro', 'barbone', 1)")

rows = cursor.execute("SELECT name, species, tank_number FROM fish").fetchall()
print(rows)

target_fish_name = "Jamie"
rows = cursor.execute("SELECT name, species, tank_number FROM fish WHERE name = ?", (target_fish_name, )).fetchall()
print(rows)

new_tank_number = 2
moved_fish_name = "Sammy"
cursor.execute("UPDATE fish SET tank_number = ? WHERE name = ?", (new_tank_number, moved_fish_name))

target_fish_name = "Sammy"
rows = cursor.execute("SELECT name, species, tank_number FROM fish WHERE name = ?", (target_fish_name, )).fetchall()
print(rows)

rows = cursor.execute("SELECT name, species, tank_number FROM fish").fetchall()
print(rows)

released_fish_name = "Sammy"
cursor.execute("DELETE FROM fish WHERE name = ?", (released_fish_name, ))

rows = cursor.execute("SELECT name, species, tank_number FROM fish").fetchall()
print(rows)

released_fish_man = "Sandro"
cursor.execute("DELETE FROM fish WHERE name = ?", (released_fish_man, ))

rows = cursor.execute("SELECT name, species, tank_number FROM fish").fetchall()
print(rows)

with closing(sqlite3.connect("aquarium.db")) as connection:
    with closing(connection.cursor()) as cursor:
        rows = cursor.execute("SELECT 1").fetchall()
        print(rows)