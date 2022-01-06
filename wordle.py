# Quick and dirty wordle solver. 
# This python script helps guess the word that was used to create the wordle.
#
# This script assumes that every word in the english language is a valid word.
# Even though this is not true, if you look the source code for wordle. 
# When you enter a invalid word, wordle will tell you. Just use the next word 
# in the list
#
# This script generates the best first word based on scoring the letters in 
# the word. According to this article that is not the best approch. Instead 
# your first two guesses should be used to reduce the amount of possiable 
# letters smaller list. For example. RAISE and PLANT. This script does not 
# take this into account.
# https://notfunatparties.substack.com/p/wordle-solver
# 
# Updated version can be found here: https://github.com/funvill/KangarooWord
#
# Play the game here
# https://www.powerlanguage.co.uk/wordle/
#
# Word list from
# https://github.com/dwyl/english-words
#


def load_words():
    with open('words_alpha.txt') as word_file:
        valid_words = set(word_file.read().split())
    return valid_words

if __name__ == '__main__':

  print("Find the best first word for wordle!") 
  print("https://www.powerlanguage.co.uk/wordle/\n")

  # Input from user
  # ============================================================ 
  # Green letters, Known location. Use '' for unknown letters.  
  green_letters = ['', 'i', '', 'e', 'r']
  # Yellow letters, In the word but not in the correct location. 
  yellow_letters = ['r', 'e', 'i', 't']
  # Gray letters. Not in the word 
  gray_letters = ['a', 'o', 's', 'm','k']

  # ============================================================

  print("Green Letters,  Know location ", green_letters)
  print("Yellow Letters, Wrong location", yellow_letters)
  print("Gray Letters,   Not in word   ", gray_letters)
  print("")

  # Load the word list
  english_words = load_words()
  print("Dictionary word count:      ", len(english_words))

  # Some words are banned by the game
  banned_word_list = ['seora']
  print("Banned word count:          ", len(banned_word_list))
  
  # Generate the english_words of words with only 5 characters
  # and remove the words that are banned by the game 
  five_word_list = list()
  for word in english_words:
    if len(word) != 5:
      continue
    if word in banned_word_list:
      continue
    five_word_list.append(word)

  print("Words with only 5 letters:  ", len(five_word_list))
  print("")


  # Find the frequency of each letter in the word list
  letter_frequency = dict()
  for word in five_word_list:
    for letter in word:
      if letter in letter_frequency:
        letter_frequency[letter] += 1
      else:
        letter_frequency[letter] = 1

  # Sort the letter frequency dictionary by value
  sorted_letter_frequency = sorted(letter_frequency.items(), key=lambda x: x[1], reverse=True)

  # Print the top 10 letters
  print("Top 10 letters: ")
  for i in range(10):
    print(sorted_letter_frequency[i][0], round(sorted_letter_frequency[i][1]/len(five_word_list)*100, 2), "%")
  print("");

  # Give each word a score based on the frequency of each letter in the word
  word_score = dict()
  for word in five_word_list:
    word_score[word] = 0
    for letter in word:
      word_score[word] += letter_frequency[letter]

  # Sort the word score dictionary by value
  sorted_word_score = sorted(word_score.items(), key=lambda x: x[1], reverse=True)

  # Print the top 10 words  
  print("Top 10 words score: ")
  for i in range(10):
    print(i + 1, sorted_word_score[i][0], sorted_word_score[i][1], "points")
  print("")

  # Find good starting words 
  # create a list of words that have no duplicated letters
  unique_word_list = list()
  for word in sorted_word_score:
    if len(set(word[0])) == 5:
      unique_word_list.append(word)

  print("Words with unique letters: ", len(unique_word_list))
  print("Top Starting words:")
  for i in range(10):
    print(i + 1, unique_word_list[i][0], sorted_word_score[i][1], "points")
  print("")

  ## ============================================================

  # Filter the word list based on the matching letters (Green)
  for word in sorted_word_score[:]:
    for i in range(5):
      if green_letters[i] == '':
        continue
      if green_letters[i] != word[0][i]:
        sorted_word_score.remove(word)
        break        
    
  print('Words that match the green letters, count: ', len(sorted_word_score))
  for i in range(10):
    if i >= len(sorted_word_score):
      break
    print(i + 1, sorted_word_score[i][0], sorted_word_score[i][1], "points")
  print("")

  
  # Filter based on the gray and yellow letters
  for word in sorted_word_score[:]:
    # Remove words with gray letters
    if any(x in word[0] for x in gray_letters):
      sorted_word_score.remove(word)
      continue

    # Remove words that don't have the all yellow letters
    if not all(x in word[0] for x in yellow_letters):
      sorted_word_score.remove(word)
      continue

  print('Words that match Yellow and Gray letters, count: ', len(sorted_word_score))
  for i in range(10):
    if i >= len(sorted_word_score):
      break
    print(i + 1, sorted_word_score[i][0], sorted_word_score[i][1], "points")
  print("")

  print("Your next guess should be:", sorted_word_score[0][0])