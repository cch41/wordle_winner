test_file = open("../data/test.txt", "r")

test_words = []
for line in test_file:
  stripped_line = line.strip()
  line_list = stripped_line.split()
  test_words.append(line_list[0])

test_file.close()

print(test_words)