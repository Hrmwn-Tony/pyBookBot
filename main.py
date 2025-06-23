from stats import word_counter, char_counter, sort_dictionary, get_report
import sys

def checkSys():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


def main():
    address = sys.argv[1]
    book = get_book_text(f"{address}")
    print(f"{word_counter(book)} words found in the document")
    charDict = char_counter(book)
    get_report(sort_dictionary(charDict), f"{address}", book)


    


def get_book_text(address):
    with open(address) as f:
        bookContent = f.read()
    return bookContent

checkSys()
main()