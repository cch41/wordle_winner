from statistics import mean

# TRAINING SET
training_words = []

training_file = open("../data/training.txt", "r")
for line in training_file:
  stripped_line = line.strip()
  line_list = stripped_line.split()
  training_words.append(line_list[0])
training_file.close()

# VALIDATION SET
validation_words = []

validation_file = open("../data/validation.txt", "r")
for line in validation_file:
  stripped_line = line.strip()
  line_list = stripped_line.split()
  validation_words.append(line_list[0])
validation_file.close()


# TEST SET
test_words = []

test_file = open("../data/test.txt", "r")
for line in test_file:
  stripped_line = line.strip()
  line_list = stripped_line.split()
  test_words.append(line_list[0])
test_file.close()


def playWordle(guessWordFunction, words):
  guess_counts = []
  for word in words:
    previous_guesses = []
    num_guesses = 0
    for _ in range(6):
        num_guesses += 1
        guess = guessWordFunction(previous_guesses)
        if guess == word:
          break      
    guess_counts.append(num_guesses)
  return mean(guess_counts)