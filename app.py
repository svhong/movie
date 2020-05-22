import os
import json

from user import User

def menu():
  name = input("Please enter a username: ")
  filename = "{}.txt".format(name)
  if file_exists(filename):
    with open(filename, 'r') as f:
      json_data = json.load(f)
      print("File successfully loaded ", json_data)
    user = User.from_json(json_data)
    print("User successfully loaded ", user)
  else:
    user = User(name)
    print("User successfully created! ", user)  

  user_input = input("Enter 'A' to add a movie, 'S' to see a list of movies, 'W' to set a movie as watched, 'D' to delete a movie, and 'L' to see a list of watched movies: ")
  if user_input == 'a':
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