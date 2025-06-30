import sys
from stats import get_book_word_count, get_character_count, get_sorted_char_arr

def get_book_text(path):
    with open(path) as file:
        book_text  = file.read()
        return book_text

def main(book_path):
    text = get_book_text(book_path)
    count = get_book_word_count(text)
    count_dict = get_character_count(text)
    sorted_char_arr = get_sorted_char_arr(count_dict)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for item in sorted_char_arr:
        if item["char"].isalpha():
            char = item["char"]
            count = item["count"]
            print(f"{char}: {count}")
    
print(sys.argv)
if (len(sys.argv) < 2): 
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
main(sys.argv[1])