import sqlite3

connection = sqlite3.connect(r'/classwork/SQL/films.sqlite')
cursor = connection.cursor()

result = cursor.execute("""SELECT title FROM films
WHERE title LIKE '%Астерикс%' AND title NOT LIKE '%Обеликс%'""")

for elem in result:
    print(*elem)
