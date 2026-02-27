import sqlite3

conn = sqlite3.connect("learning2.db")
cursor = conn.cursor()

cursor.execute("PRAGMA foreign_keys = ON")

cursor.execute("""
CREATE TABLE IF NOT EXISTS characters (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE,
    age INTEGER,
    gender TEXT,
    birth_year INTEGER
)
""")

cursor.execute("""
INSERT INTO characters (name, age, gender, birth_year)
    VALUES (?, ?, ?, ?)
""", ("Freia", 16, "Female", 1810))

conn.commit()

cursor.execute("SELECT * FROM characters")
rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.execute("""
UPDATE characters
               SET age = ?
               WHERE name = ?
""", (17, "Freia"))
conn.commit()


cursor.execute("""
INSERT INTO characters (name, age, gender, birth_year)
               VALUES(?, ?, ?, ?)
""", ("Bellona", 16, "Female", 1798))
conn.commit()


# cursor.execute("""
# DELETE FROM characters
#                WHERE name = ?
# """, ("Freia",))
# conn.commit()


cursor.execute("""
INSERT INTO characters (name, age, gender, birth_year)
               VALUES(?, ?, ?, ?)
""", ("Rein", 40, "Male", 1786))
conn.commit()


cursor.execute("""
INSERT INTO characters (name, age, gender, birth_year)
               VALUES(?, ?, ?, ?)
""", ("Amilla", 39, "Female", 1787))
conn.commit()

def print_all():
    cursor.execute("SELECT * FROM characters")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
print("------")

print_all()


cursor.execute("""
CREATE TABLE IF NOT EXISTS relations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    character_id INTEGER,
    related_character_id INTEGER,
    relation_type TEXT,
    FOREIGN KEY (character_id) REFERENCES characters(id) ON DELETE CASCADE,
    FOREIGN KEY (related_character_id) REFERENCES characters(id) ON DELETE CASCADE
)
""")

# cursor.execute("SELECT id FROM characters WHERE name = ?", ("Freia",))
# freia_row = cursor.fetchone()

# cursor.execute("SELECT id FROM characters WHERE name = ?", ("Bellona",))
# bellona_row = cursor.fetchone()

# cursor.execute("SELECT id FROM characters WHERE name = ?", ("Rein",))
# rein_row = cursor.fetchone()

# cursor.execute("SELECT id FROM characters WHERE name = ?", ("Amilla",))
# amilla_row = cursor.fetchone()


# if freia_row and bellona_row and rein_row and amilla_row:
#     freia_id = freia_row[0]
#     bellona_id = bellona_row[0]
#     rein_id = rein_row[0]
#     amilla_id = amilla_row[0]

#     cursor.execute("""
#     INSERT INTO relations (character_id, related_character_id, relation_type)
#                 VALUES (?, ?, ?)
#     """, (freia_id, bellona_id, "siblings"))
#     conn.commit()

ids = {}

for name in ["Freia", "Bellona", "Rein", "Amilla"]:
    cursor.execute("SELECT id FROM characters WHERE name = ?", (name,))
    row = cursor.fetchone()
    if row:
        ids[name] = row[0]

if "Freia" in ids and "Bellona" in ids:
    cursor.execute("""
        INSERT INTO relations (character_id, related_character_id, relation_type)
        VALUES (?, ?, ?)
""", (ids["Freia"], ids["Bellona"], "siblings"))
    conn.commit()


cursor.execute("""
SELECT c1.name, r.relation_type, c2.name
    FROM relations r
    JOIN characters c1 ON r.character_id = c1.id
    JOIN characters c2 ON r.related_character_id = c2.id
""")

rows = cursor.fetchall()

for row in rows:
    print(row)

# cursor.execute("""
# SELECT c.name
#     FROM characters c
#     LEFT JOIN relations r1 ON c.id = r1.character_id
#     LEFT JOIN relations r2 ON c.id = r2.related_character_id
#     WHERE r1.id IS NULL
#     AND r2.id IS NULL;
# """)

cursor.execute("""
SELECT name
    FROM characters c
    WHERE NOT EXISTS (
    SELECT 1
    FROM relations r
    WHERE c.id = r.character_id
    OR c.id = r.related_character_id
);
""")

rows = cursor.fetchall()

for row in rows:
    print(row)


cursor.execute("""
SELECT c.name, COUNT(r.id) AS total_relations
               FROM characters c
               LEFT JOIN relations r
               ON c.id = r.character_id
               GROUP BY c.id, c.name;
""")

rows = cursor.fetchall()
for row in rows:
    print(row)

conn.close()