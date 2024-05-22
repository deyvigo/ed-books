import json

import sys
from os.path import dirname, abspath

# Añadir el directorio src al sys.path
sys.path.insert(0, dirname(dirname(abspath(__file__))))

from models import GenreModel, AuthorModel

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


# print(genres_set)

for genre in genres_set:
  GenreModel().post_one_genre(genre)

for author in author_set:
  AuthorModel().post_one_author(author)

print(author_set)