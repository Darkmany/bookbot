def get_book_text(path):
    with open(path) as book:
        book_text = book.read()
    return book_text

def main():
    text = get_book_text("books/frankenstein.txt")
    print(text)

main()