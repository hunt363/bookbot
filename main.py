from stats import get_word_count
from stats import get_char_count
import sys

def get_book_text(path):
    with open(path) as book:
        return book.read()

if __name__=="__main__":
    if len(sys.argv)!=2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)   
    word_count=get_word_count(get_book_text(sys.argv[1]))
    char_count_dict=get_char_count(get_book_text(sys.argv[1]))
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char, count in char_count_dict.items():
        if char.isalpha():
            print(f"{char}: {count}")
    print("============= END ===============")
        
        
    