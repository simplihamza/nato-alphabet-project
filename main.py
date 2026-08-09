import pandas

nato_alphabets = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_helper = {row.letter:row.code for (index, row) in nato_alphabets.iterrows()}

user_input = input("Enter the word or name: ").upper()
#
# for letter in user_input:
#     if letter in phonetic_helper["letter"]:
#         print(phonetic_helper[letter])

# TODO: Use a LIST comprehension to build a list of NATO code words —
#  one for each letter in the user's input word, by looking each letter
#  up in your dictionary.