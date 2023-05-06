import pandas
import numpy

# student_dict = {
#     "student": ["Angela", "James", "Lily", "Pablo"],
#     "score": [56, 76, 98, numpy.nan]
# }
# for (key, value) in student_dict.items():
#     print(key)
#     print(value[0])
#Loop through rows of a data frame
# student_data_frame = pandas.DataFrame(student_dict)
# for (index, row) in student_data_frame.iterrows():
#     print(row.student)
#     print(row.score)

data = pandas.read_csv("nato_phonetic_alphabet.csv")

# print(data.to_dict())

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
dict = {row.letter: row.code for (index, row) in data.iterrows()}


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ").upper()

result = [dict[letter] for letter in word]
print(result)



