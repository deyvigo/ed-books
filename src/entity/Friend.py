class Friend:
  def __init__(self, id_friend, id_applicant, id_receiver, is_accept):
    self.id_friend = id_friend
    self.id_applicant = id_applicant
    self.id_receiver = id_receiver
    self.is_accept = is_accept

  def __repr__(self):
    return f"{self.id_friend}"
  
  def to_json(self):
    return { "id_friend": self.id_friend, "id_applicant": self.id_applicant, "id_receiver": self.id_receiver, "is_accept": self.is_accept }