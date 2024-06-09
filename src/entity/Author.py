class Author:
  def __init__(self, name, id_author) -> None:
    self.name = name
    self.id_author = id_author

  def __repr__(self) -> str:
    return f"{self.name}"
  
  def to_json(self):
    return { "name": self.name, "id_author": self.id_author } 