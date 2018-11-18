class Message:
  def __init__(self,user,message,time,id):
    self.user = user
    self.message = message
    self.time = time
    self.id = id

  def get_user(self):
    return self.user

  def get_message(self):
    return self.message

  def get_time(self):
    return self.time

  def get_id(self):
    return self.id

  def toString(self):
    return (f"ID: {self.id} User: {self.user} Message: {self.message} Time: {self.time} ")