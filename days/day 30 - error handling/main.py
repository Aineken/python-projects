import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
dict = {row.letter: row.code for (index, row) in data.iterrows()}


# TODO 2. Create a list of the phonetic code words from a word that the user inputs.


def ask_name():
    word = input("Enter a word: ").upper()
    try:
        result = [dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        ask_name()
    else:
        print(result)


ask_name()
