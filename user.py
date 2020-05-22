from movie import Movie

class User:
  def __init__(self, name):
    self.name = name
    self.movies = []

  def __repr__(self):
    return "<User {}>".format(self.name)

  def add_movie(self, name, genre):
    movie = Movie(name, genre, False)
    self.movies.append(movie)
    print("Successfully added movie!")

  def delete_movie(self, name):
    self.movies = list(filter(lambda movie: movie.name != name, self.movies))

  def watched_movies(self):
    movies_watched = list(filter(lambda movie: movie.watched, self.movies))
    return movies_watched
    # calculate a list of movies that have been watched
    # watched_movies_list = []
    # iterate over self.movies
    # if movie.watched is true, add to list
    # return list
    # for movie in self.movies:
    #   if movie.watched:
    #     watched_movies_list.append(movie)
    # return watched_movies_list

  def json(self):
    return {
      'name': self.name,
      'movies': [
        movie.json() for movie in self.movies
      ]
    }
  # def save_to_file(self):
  #   with open("{}.txt".format(self.name), 'w') as f:
  #     f.write(self.name + "\n")
  #     for movie in self.movies:
  #       f.write("{},{},{}\n".format(movie.name, movie.genre, str(movie.watched)))

  # @classmethod
  # def load_from_file(cls, filename):
  #   with open(filename, 'r') as f:
  #     content = f.readlines() #gives us list of lines read
  #     username = content[0]
  #     movies = []
  #   for line in content[1:]:
  #     movie_data = line.split(",") # split the line of comma
  #     movies.append(Movie(movie_data[0],movie_data[1], movie_data[2] == "True")) # beacuse movie.watched is a boolean
  #   user = cls(username)
  #   user.movies = movies
  #   return user
  @classmethod
  def from_json(cls, json_data):
    user = cls(json_data['name'])
    movies = []
    for movie_data in json_data['movies']:
      movies.append(Movie.from_json(movie_data))
    user.movies = movies

    return user