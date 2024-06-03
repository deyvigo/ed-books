class Genre:
  def __init__(self, genre_name, id_genre) -> None:
    self.genre_name = genre_name
    self.id_genre = id_genre

  def __repr__(self) -> str:
    return f"{self.genre_name}"
  
  def to_json(self):
    return { "id_genre": self.id_genre, "genre_name": self.genre_name }