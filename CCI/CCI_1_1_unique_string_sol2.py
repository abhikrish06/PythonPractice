# Determine whether or not a given string contains no duplicate characters.
# https://github.com/w-hat/ctci-solutions/blob/master/ch-01-arrays-and-strings/01-is-unique.py

def contains_no_duplicates(string):
  letters = {}
  for letter in string:
    if letter in letters:
        return False
    letters[letter] = string.count(letter) #.count() counts the occurance of each letter in a sting at once..not iteratively
    print(letters)
  return True

print(contains_no_duplicates("abhikrish"))
#if __name__ == "__main__":
#  import sys
#  print(contains_no_duplicates(sys.argv[-1]))

# for info on sys.argv[-1] visit https://stackoverflow.com/questions/4117530/sys-argv1-meaning-in-script