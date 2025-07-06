import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def main():
    path = sys.argv[1]
    text = get_book_text(path)
    count = word_count(text)
    chars = char_count(text)
    sort = sort_chars(chars)
    print(f"""============ BOOKBOT ============
    Analyzing book found at {path}...
    ----------- Word Count ----------
    Found {count} total words
    --------- Character Count -------""")
    for diction in sort:
        if diction["char"].isalpha() == True:
            print(f"{diction["char"]}: {diction["num"]}")
    print("============= END ===============")

def get_book_text(path):
    with open(path) as book:
        return book.read()

from stats import word_count, char_count, sort_chars



main()