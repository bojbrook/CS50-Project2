class Message:
  def __init__(self,user,message):
    self.user = user
    self.message = message

  def get_user(self):
    return self.user

  def get_message(self):
    return self.message

  def toString(self):
    return (f"User: {self.user} Message: {self.message}")