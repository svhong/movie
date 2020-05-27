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
      # need a real success / error message here
      print("Successfully loaded json from file!")
    user = User.from_json(json_data)
    print("Welcome back, {}!".format(user.name))
  else:
    user = User(name)
    print("User successfully created! ", user)  
  print ('*' * 100)
  user_input = input("'a' - Add a movie.\n's' - See list of movies.\n'w' - Set movie as watched.\n'd' - Delete a movie.\n'e' - List of watched movies.\n'q' - Exit the app.\nYour Selection: ")
  print ('*' * 100)
  while user_input != 'q':
    if user_input == 'a':
      name = input("Please enter the title of the movie: ")
      genre = input("Please enter the genre: ")
      user.add_movie(name, genre)
      with open(filename, 'w') as f:
        json.dump(user.json(), f)
        # need a real success / error message here
        print("Movie added successfully!")
        print ('*' * 100)
      pass
    elif user_input == 's':
      print (user.movies)
      pass
    elif user_input == 'w':
      pass
    elif user_input == 'd':
      print(user.movies)
      name = input("Name of movie to delete: ")
      user.delete_movie(name)
      with open(filename, 'w') as f:
        json.dump(user.json(), f)
        # need a real success / error message here
        print("Movie deleted successfully!")
      print(user.movies)
      print ('*' * 100)
      pass
    elif user_input == 'q':
      return
    user_input = input("'a' - Add a movie.\n's' - See list of movies.\n'w' - Set movie as watched.\n'd' - Delete a movie.\n'e' - List of watched movies.\n'q' - Exit the app.\nYour Selection: ")
    print ('*' * 100)


def file_exists(filename):
  return os.path.isfile(filename)

menu()