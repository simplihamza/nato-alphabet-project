import pandas
nato_alphabets = pandas.read_csv("nato_phonetic_alphabet.csv")
data_frame = pandas.DataFrame(nato_alphabets)

phonetic_helper = {index:row for (index, row) in data_frame.iterrows()}
print(phonetic_helper)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

