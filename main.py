from stats import count_words, char_count, get_sorted
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        txt = f.read()
    return txt


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    pathname = sys.argv[1]
    display_text = get_book_text(pathname)
    num_of_words = count_words(display_text)
    char_dict = char_count(display_text)
    print(f"""============ BOOKBOT ============
Analyzing book found at {pathname}...
----------- Word Count ----------""")
    print(f"Found {num_of_words} total words")
    print("""--------- Character Count -------""")
    char_dict_list = get_sorted(char_dict)
    for info in char_dict_list:
        if info["name"].isalpha():
            print(f"{info["name"]}: {info["num"]}")
    print("""============= END =============== """)

main()
