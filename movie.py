class Movie:
  def __init__(self, name, genre, watched):
    self.name = name
    self.genre = genre
    self.watched = watched
  
  def __repr__(self):
    return "<Movie {}>".format(self.name)
  
  def json(self):
    return {
      'name': self.name,
      'genre': self.genre,
      'watched': self.watched
    }
  
  @classmethod
  def from_json(cls, json_data):
    # dictionaries are not in order therefore we can use named by adding name=json_data['name'] as the parameter
    # return Movie(json_data['name'], json_data['genre'], json_data['watched'])
    # it can instead be give argument unpacker
    return Movie(**json_data)