import sys
from stats import count_words, count_characters, sort_dict


def get_book_text(path: str) -> str:
    with open(path) as f:
        file_contents = f.read()
    return file_contents


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]

    num_words = count_words(get_book_text(path))
    chars_dict = count_characters(get_book_text(path))
    sorted_list_of_dicts = sort_dict(chars_dict)
    print("============ BOOKBOT ============")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for dict in sorted_list_of_dicts:
        print(f"{dict["char"]}: {dict["num"]}")
    print("============= END ===============")


main()
