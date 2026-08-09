import pandas

nato_alphabets = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_data = {row.letter:row.code for (index, row) in nato_alphabets.iterrows()}

# Taking an input from the user to later convert it into nato phonetic alphabet
user_input = input("Enter the word or name: ").upper()

phonetic_helper = [phonetic_data[word] for word in user_input if word in phonetic_data]
print(phonetic_helper)