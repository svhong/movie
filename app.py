import os
import json

from user import User

def menu():
  # check user and create file if new user
  name = input("Please enter a username: ")
  filename = "{}.txt".format(name)
  if file_exists(filename):
    with open(filename, 'r') as f:
      json_data = json.load(f)
      print("Successfully loaded json from file!")
    user = User.from_json(json_data)
    print("Welcome back, {}!".format(user.name))
  else:
    user = User(name)
    print("User successfully created! ", user)  

  # provide user with menu
  user_input = input(" 'a' - Add Movie \n 's' - See your list of movies \n 'w' - Mark a movie as watched \n 'd' - Remove a movie from your list \n 'e' - Show list of all watched: ")
  if user_input == 'a':
    name = input("Please enter the title of the movie: ")
    genre = input("Please enter the genre: ")
    user.add_movie(name, genre)
    with open(filename, 'w') as f:
      json.dump(user.json(), f)
      print("Movie added successfully!")
    pass
  elif user_input == 's':
    print (user.movies)
    pass
  elif user_input == 'w':
    pass
  elif user_input == 'd':
    pass
  elif user_input == 'q':
    return


def file_exists(filename):
  return os.path.isfile(filename)

menu()