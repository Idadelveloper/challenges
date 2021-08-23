def get_letter(plate):
    letters = []
    for char in plate:
        if char.isalpha() == True:
            letters.append(char)
    return letters


def get_matches(word, letters):
    count = 0
    for letter in letters:
        if len(word) == len(set(word)):
            if letter in word:
                count +=1
        else:
            for char in word:
                if char == letter:
                    count += 1
    return (word, len(word), count)


def find_shortest_word(plate, vocabulary):
  """Return the shortest word in the vocabulary with all the letters in a license plate."""
  if len(vocabulary) <= 0 or type(vocabulary) != list:
    return ""
  letters = get_letter(plate)
  final = []
  for word in vocabulary:
      if len(final) == 0:
          final.append(get_matches(word.upper(), letters))
      else:
          temp = get_matches(word.upper(), letters)
          if temp[2] > final[0][2] or (temp[2] == final[0][2] and temp[1] < final[0][1]):
              final.pop()
              final.append(temp)
          else:
              continue

  return final[0][0].lower()

  