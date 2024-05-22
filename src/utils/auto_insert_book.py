import json

with open("src/mocks/books.json", "r") as file:
  books_data = json.load(file)
# Falta Cumbres Borrascosas

genres_set = set()
author_set = set()

for book_data in books_data:
  for genre in book_data["genre"]:
    genres_set.add(genre)

  for author in book_data["author"]:
    author_set.add(author)


print(genres_set)
print(author_set)