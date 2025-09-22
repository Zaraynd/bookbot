import sys

from stats import get_num_words
from stats import get_num_char
from stats import sort_char_list


def get_book_text (filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        file_content = f.read()
    return file_content

def main ():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_address = sys.argv[1]
    book_text = get_book_text(book_address)
    word_count = get_num_words(book_text)
    char_count = get_num_char(book_text)
    sorted_list = sort_char_list(char_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_address}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char in sorted_list:
        print(f"{char['char']}: {char['num']}")
    return

if __name__ == "__main__":
    main()
