import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    pass

student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # Access index and row
    # Access row.student or row.score
    pass
# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
df = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {value.letter: value.code for (key, value) in df.iterrows()}
print(nato_dict)


# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_word = input("Please type a word in: ")
nato_list = [nato_dict[letter.capitalize()] for letter in user_word]

print(nato_list)
