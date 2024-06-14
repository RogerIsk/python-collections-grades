# Task. You have a dict with a list of book titles as keys and their sales numbers as values. 
# Implement a method that prints the top 3 books from this dict to the screen.


books = {
  'Harry Potter And The Sorcerer\'s Stone': 1241100000,
  'Harry Potter And The Chamber Of Secrets': 771300000,
  'Harry Potter And The Prisoner Of Azkaban': 65210000,
  'Harry Potter And The Goblet Of Fire': 645600000,
  'Harry Potter And The Order Of The Phoenix': 635600000,
  'Harry Potter And The Half Blood Prince': 661300000,
  'Harry Potter And The Deathly Hallows ': 652200000,
}

def display_first_three_movies(books):
    
    movie_titles = list(books.keys())      # Extract the keys (movie titles) from the dictionary
    first_three_movies = movie_titles[:3]  # Slice the list to get the first three movie titles
    for movie in first_three_movies:       # Print the first three movies
        print(movie)

display_first_three_movies(books)