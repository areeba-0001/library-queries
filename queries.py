import sqlite3

conn = sqlite3.connect("library.db")
cur = conn.cursor()

print("Books above Rs.1000 (sorted):")

cur.execute("""
SELECT title, price
FROM books
WHERE price > 1000
ORDER BY price DESC;
""")

for row in cur.fetchall():
    print(row)


print("\nTitles using AS:")

cur.execute("""
SELECT title AS book_title
FROM books;
""")

for row in cur.fetchall():
    print(row)


print("\nLow-stock Fiction books:")

cur.execute("""
SELECT title, genre, price, stock
FROM books
WHERE genre = 'Fiction' AND stock < 5;
""")

for row in cur.fetchall():
    print(row)

conn.close()
