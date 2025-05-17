"""
get_book_text takes a filepath as input and returns the contents of the file as a string.
"""

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def main():
    from stats import count_words, count_char, sorted_list
    import sys
 
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    text = get_book_text(book_path)
    word_count = count_words(text)
    char_dict = count_char(text)
    dict_list = sorted_list(char_dict)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for dict in dict_list:
        if dict["char"].isalpha():
            print(f"{dict["char"]}: {dict["num"]}")

    print("--------- Character Count -------")

if __name__ == "__main__":
    main()