import sqlite3

connection = sqlite3.connect(r'C:\Users\danya\PycharmProjects\3-й семестр\classwork\SQL\films.sqlite')
cursor = connection.cursor()

result = cursor.execute("""SELECT title FROM films
WHERE duration <=85""")

for elem in result:
    print(*elem)