from entity import Author, Genre

class Book:
  def __init__(self, id, title, description, url_img) -> None:
    self.id = id
    self.title = title
    self.description = description
    self.url_img = url_img
    self.author: list[Author] = []
    self.genres: list[Genre] = []

  def __repr__(self) -> str:
    return f"{self.title}"
  
  def to_json(self):
    return { "id_book": self.id, "title": self.title, "description": self.description, "url_img": self.url_img, "author": [a.to_json() for a in self.author], "genres": [g.to_json() for g in self.genres] }