# NATO Phonetic Alphabet Converter 🔤

# NATO Phonetic Alphabet Converter 🔤

A Python program that converts any word into its NATO phonetic alphabet equivalent (e.g., "Python" → Papa Yankee Tango Hotel Oscar November).

## Features
- Loads the NATO phonetic alphabet data from a CSV file using `pandas`
- Takes any word or name as user input
- Converts each letter into its corresponding NATO phonetic code word using a list comprehension
- Prints the full phonetic spelling of the input word
- Handles invalid input gracefully; if a character isn't part of the NATO alphabet (e.g. punctuation or spaces), the user is prompted to try again instead of the program crashing

## How to Run
1. Clone or download this repository to your device.
2. Make sure you have Python installed (3.x recommended) along with the `pandas` library:

## pip install pandas
3. Make sure `nato_phonetic_alphabet.csv` is in the same folder as `main.py`.
4. Run `main.py`:

## python main.py
5. Enter any word or name when prompted, and see its NATO phonetic spelling printed out.

## How I Got Here

Before writing this project's actual logic, I spent time practicing list and dictionary comprehensions in a separate file (`learning_and_practice.py`); starting with simple transforms and filtering on lists, then moving on to building and filtering dictionaries, including converting data read from files and applying random values. That practice directly fed into this project: I used a dictionary comprehension (paired with `pandas.iterrows()`) to turn the NATO phonetic alphabet CSV into a clean, lookup-ready dictionary, then used a list comprehension to convert user input into its phonetic spelling.

## What I Learned
- Reading CSV data into a `pandas` DataFrame
- Understanding exactly what `.iterrows()` returns (an index and a row object), and correctly accessing specific columns off of each row
- Building a dictionary using dictionary comprehension as a fast lookup table
- Converting user input into a transformed list using list comprehension
- Filtering out invalid characters (e.g., spaces or symbols not in the alphabet) directly within the list comprehension
- Using `try`/`except` to catch and handle a `KeyError` gracefully instead of letting the program crash
- Using a `while True` loop with `break` to keep retrying an operation until it succeeds
- Debugging a scope-related bug where a variable was referenced outside the `try` block where it was assigned, causing a `NameError` when the assignment failed