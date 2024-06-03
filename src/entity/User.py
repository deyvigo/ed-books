class User:
  def __init__(self, id_user, name, username, password) -> None:
    self.id_user = id_user
    self.name = name
    self.username = username
    self.password = password

  def __repr__(self) -> str:
    return f"{self.username}"
  
  def to_json(self):
    return { "id_user": self.id_user, "name": self.name, "username": self.username, "password": self.password }

  def to_json_ommit_password(self):
    return { "id_user": self.id_user, "name": self.name, "username": self.username } 