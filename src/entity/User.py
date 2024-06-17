class User:
  def __init__(self, username, password, name, id_user) -> None:
    self.username = username
    self.password = password
    self.name = name
    self.id_user = id_user

  def to_json(self):
    return {
      "id_user" : self.id_user,
      "username" : self.username,
      "password" : self.password,
      "name" : self.name
    }

  def __repr__(self) -> str:
    return f"{self.username}"

  def to_json_ommit_password(self):
    return { "id_user": self.id_user, "name": self.name, "username": self.username } 
