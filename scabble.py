letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letter_to_points = {key:value for key, value in zip(letters, points)}
letter_to_points[" "] = 0
print(letter_to_points)

def score_word(word):
  point_total = 0
  for letter in word.upper():
    point_total += letter_to_points.get(letter, 0)
  return point_total
brownie_points = "BROWNIE"
print(score_word(brownie_points))

player_to_words = {'player1': ['BLUE', 'TENNIS', 'EXIT'], 'wordNerd': ['EARTH', 'EYES', 'MACHINE'], 'Lexi Con': ['ERASER', 'BELLY', 'HUSKY'], 'Prof Reader': ['ZAP', 'COMA', 'PERIOD']}

def update_point_totals(dictionary): 
  player_to_points = {}
  for player, words in dictionary.items():
    player_points = 0
    for word in words:
      player_points += score_word(word)
    player_to_points[player] = player_points
  return player_to_points
print(update_point_totals(player_to_words))

def play_word(player, word, dictionary):
  if player in dictionary:
    dictionary[player].append(word)
  else:
    dictionary[player] = [word]
  return dictionary
  
print(play_word('player1', 'LOVE', player_to_words))