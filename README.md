# NATO Phonetic Alphabet Converter 🔤

A Python program that converts any word into its NATO phonetic alphabet equivalent (e.g., "Python" → Papa Yankee Tango Hotel Oscar November).

> 🚧 **Work in progress** — this project is being built incrementally. Check the commit history for the latest progress and features added.

## Features (planned / in progress)
- [x] Load the NATO phonetic alphabet data from a CSV file using `pandas`
- [ ] Take a word as user input
- [ ] Convert each letter of the input word into its corresponding NATO code word
- [ ] Display the final phonetic spelling to the user

## How to Run
1. Clone or download this repository to your device.
2. Make sure you have Python installed (3.x recommended) along with the `pandas` library:

## pip install pandas
3. Make sure `nato_phonetic_alphabet.csv` is in the same folder as `main.py`.
4. Run `main.py`:

## python main.py
## What I'm Learning
- Reading CSV data into a `pandas` DataFrame
- Converting DataFrame rows into a usable Python dictionary (e.g., using `.iterrows()`)
- Building a lookup-based text conversion tool

## How I Got Here

Before writing this project's actual logic, I spent time practicing list and dictionary comprehensions in a separate file (`learning_and_practice.py`) — starting with simple transforms and filtering on lists, then moving on to building and filtering dictionaries, including converting data read from files and applying random values. That practice directly fed into this project: I used a dictionary comprehension (paired with `pandas.iterrows()`) to turn the NATO phonetic alphabet CSV into a clean, lookup-ready dictionary — the foundation the rest of this project builds on.