import sys

def word_count(string_of_book):
    new_text = string_of_book.split()
    word_count = len(new_text)
    return (f"Found {word_count} total words")

def character_count(string_of_book):
    characters = {}
    text_fixed = string_of_book.lower()
    for letter in text_fixed:
        if letter not in characters:
            characters[letter] = 1

        else :
            characters[letter] += 1

    return characters

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def sort_characters(test_dict):
    new_list = []
    while test_dict != {}:
        counter = 0
        highest_count = " "
        for character in test_dict:
            if test_dict[character] > counter:
                counter = test_dict[character]
                highest_count = character

        new_list.append({"char": highest_count, "num": counter})
        del test_dict[highest_count]

    return new_list


# one = word_count("books/frankenstein.txt")
# two = character_count("books/frankenstein.txt")
# three = sort_characters(two)