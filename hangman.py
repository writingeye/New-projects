# -*- coding: utf-8 -*-

import random
from bs4 import BeautifulSoup
import requests
import string
print("importing done!")

# movie_list = ['The Godfather', 'The Shawshank Redemption', "Schindler's List", 'Raging Bull', 'Casablanca', 'Citizen Kane', 'Gone with the Wind', 'The Wizard of Oz', "One Flew Over the Cuckoo's Nest",
#               'Lawrence of Arabia','Vertigo', 'Psycho', 'The Godfather Part II', 'On the Waterfront' 'Sunset Blvd.', 'Forrest Gump', 'The Sound of Music', '12 Angry Men', 'West Side Story',
#                'Star Wars: Episode IV - A New Hope', '2001: A Space Odyssey', 'E.T.', 'The Silence of the Lambs', 'Chinatown', 'The Bridge on the River Kwai', "Singin' in the Rain", "It's a Wonderful Life",
#                'Dr. Strangelove or: How I Learned to Stop Worrying and Love the Bomb', 'Some Like It Hot', 'Ben-Hur',  'Apocalypse Now', 'Amadeus', 'The Lord of the Rings: The Return of the King', 'Gladiator',
#                'Titanic', 'From Here to Eternity', 'Saving Private Ryan', 'Unforgiven', 'Raiders of the Lost Ark', 'Rocky', 'A Streetcar Named Desire', 'The Philadelphia Story', 'To Kill a Mockingbird',
#                'An American in Paris', 'The Best Years of Our Lives', 'My Fair Lady',  'A Clockwork Orange', 'Doctor Zhivago', 'The Searchers', 'Jaws', 'Patton', 'Butch Cassidy and the Sundance Kid',
#               'The Treasure of the Sierra Madre',  'The Good, the Bad and the Ugly', 'The Apartment', 'Platoon', 'High Noon', 'Braveheart', 'Dances with Wolves', 'Jurassic Park', 'The Exorcist', 'The Pianist',
#               'Goodfellas', 'The Deer Hunter', 'All Quiet on the Western Front', 'Bonnie and Clyde', 'The French Connection', 'City Lights', 'It Happened One Night', 'A Place in the Sun', 'Midnight Cowboy',
#                'Mr. Smith Goes to Washington', 'Rain Man', 'Annie Hall', 'Fargo', 'Giant', 'Shane', 'The Grapes of Wrath', 'The Green Mile', 'Close Encounters of the Third Kind', 'Nashville', 'Network',
#               'The Graduate', 'American Graffiti', 'Pulp Fiction', 'Terms of Endearment', 'Good Will Hunting', 'The African Queen',  'Stagecoach', 'Mutiny on the Bounty', 'The Great Dictator', 'Double Indemnity',
#               'The Maltese Falcon', 'Wuthering Heights', 'Taxi Driver', 'Rear Window', 'The Third Man', 'Rebel Without a Cause', 'North by Northwest', 'Yankee Doodle Dandy']
# movie = random.choice(movie_list)

hindi_movie= ["Dangal","Baahubali","Pathaan",
             "Bajrangi Bhaijaan","Secret Superstar","sultan",
             "sanju","Padmaavat","tiger zinda hai", "Andhadhun"
             ,"three idiots","chennia express","kabir singh"
             ,"ratan dhan payo","drishyam","ek tha tiger",
              "rocky aur rani kii prem kahaani",
             ]

pick_title = random.choice(hindi_movie)
pick_title

# Get top 100 movies from IMDB
def get_movie_titles():
    url = "https://www.imdb.com/list/ls055592025/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content,"html.parser")
    content = soup.find_all("h3",class_="lister-item-header")
    title =[]
    for id,movie in enumerate (content,1):
        movie_titles = movie.find("a").get_text()

        title.append(movie_titles)

    return title

def Hangman(language,lives):

  language = language.lower().strip()
  if language == "english":

    global all_titles
    all_titles = get_movie_titles()
    pick_title = random.choice(all_titles)
    pick_title

  elif language == "hindi":
    pick_title = random.choice(hindi_movie)
    pick_title

  else:
    return "please enter English or Hindi"




  pick_word = pick_title.lower()
  word = ["_" if i == " " else i for i in pick_word]
  word_letters = set(word)
  alphabets = set(string.ascii_lowercase)
  used_letters = set(["a","e","i","o","u","_"])


  print("You have", lives, "lives left. Used letters: ",
        " ".join(used_letters))

  word_list = [i if i in used_letters else "-" for i in word]
  print(word_list)
  while "-" in word_list and lives > 0:
    #Ask for user input
    user_letter = input("Enter an alphabet: ")
    if user_letter in alphabets - used_letters:
      used_letters.add(user_letter)
      if user_letter in word_letters:
        word_letters.remove(user_letter)
        user_letter.join(used_letters)
      else:
        lives = lives -1
        print('\n Your letter',user_letter,"not in word")
    elif user_letter in used_letters:
      print("You have already guessed that letter")

    else:
      print("You have entered an in valid character")

    word_list = [i if i in used_letters else "-" for i in word]
    print(word_list)
    print(lives)

  if lives == 0:
    print(f"Sorry, you lose! The word was: {pick_word}")
  elif "-" not in word_list:
    print("Yon Win!")

Hangman("English",3)