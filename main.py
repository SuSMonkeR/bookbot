from stats import word_count
from stats import character_count
from stats import get_book_text
from stats import sort_characters
import sys



def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    book_text = get_book_text(sys.argv[1])
    char_count = character_count(book_text)
    char_sorted = sort_characters(char_count)
    # print(get_book_text(sys.argv[1]))
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(word_count(book_text))
    print("--------- Character Count -------")
    for item in char_sorted:
         if item['char'].isalpha() == True:
             print(f"{item['char']}: {item['num']}")
    print("============= END ===============")


main()
