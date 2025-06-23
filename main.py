from stats import word_counter, char_counter, sort_dictionary, get_report
def main():
    book = get_book_text("books/frankenstein.txt")
    print(f"{word_counter(book)} words found in the document")
    charDict = char_counter(book)
    get_report(sort_dictionary(charDict), "books/frankenstein.txt", book)


    


def get_book_text(address):
    with open(address) as f:
        bookContent = f.read()
    return bookContent


main()