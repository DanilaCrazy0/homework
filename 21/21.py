import sqlite3

connection = sqlite3.connect('music_db.sqlite')
cursor = connection.cursor()

genre = input('Введите жанр: ')
result_albums = list(cursor.execute(f"""SELECT title FROM Album
WHERE AlbumId in (SELECT AlbumId FROM Track
WHERE GenreId = (SELECT GenreId FROM Genre
WHERE Name = '{genre}'))"""))
result_albums = list(map(lambda a: str(a)[2:-3], result_albums))

artist_result = list(cursor.execute(f"""SELECT ArtistId FROM Album
WHERE AlbumId in (SELECT AlbumId FROM Track
WHERE GenreId = (SELECT GenreId FROM Genre
WHERE Name = '{genre}'))"""))
artist_result = list(map(lambda a: str(a)[1:-2], artist_result))

artist_album = []
for artist, album in zip(artist_result, result_albums):
    artist_album.append((int(artist), album))
artist_album.sort()

for i in range(len(artist_album)):
    print(artist_album[i][1])