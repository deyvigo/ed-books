import json

import sys
from os.path import dirname, abspath

# Añadir el directorio src al sys.path
sys.path.insert(0, dirname(dirname(abspath(__file__))))

from models import GenreModel, AuthorModel, BookModel, BookGenreModel

with open("src/mocks/books.json", "r", encoding="ISO-8859-1") as file:
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
  GenreModel().post_one_genre(genre) # <-- insert genre

for author in author_set:
  AuthorModel().post_one_author(author) # <-- insert author

genres = GenreModel().get_all_genre()
authors = AuthorModel().get_all_author()

# print(genres)
# print(authors)

new_books_data = []

for book_data in books_data:
  book = {
    "name": book_data["title"],
    "url_img": book_data["url_img"],
    "description": book_data["description"]
  }

  for author in authors['data']:
    if author['name'] in book_data["author"]:
      book["id_author"] = author["id_author"]
  
  new_books_data.append(book)

for book in new_books_data:
  msg = BookModel().post_one_book(book["name"], book["id_author"], book["description"], book["url_img"]) # <-- insert book
#   print(msg)

# print(author_set)


book_genre = []

books = BookModel().get_all_book()
# print(genres)

for book in books['data']:
  for book_data in books_data:
    if (book["name"] == book_data["title"]):
      # print(f"{book['name']} {book['id_book']}")
      for genre in genres['data']:
        if genre["genre_name"] in book_data["genre"]:
          # print(f"{book['id_book']} {genre['id_genre']}")
          book_genre.append([book['id_book'], genre['id_genre']])

# print(book_genre)

for data in book_genre:
  BookGenreModel().post_one_book_genre(data[0], data[1])
