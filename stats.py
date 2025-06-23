def word_counter(book):
    bookSplitted = book.split()
    return len(bookSplitted)

def char_counter(book):
    charSets = {'a'}
    charDict = {'a' : 1}
    for char in book.lower():
        if char in charSets:
            charDict[char] += 1
        else:
            charDict[char] = 1
            charSets.add(char)

    return charDict

def sort_dictionary(charDict):
    sortedDict = []
    for key in charDict:
        sortedDict.append({"char":key, "num": charDict[key]})
    sortedDict.sort(key= lambda item: item["num"], reverse = True)
    return sortedDict

def get_report(charDict, address, originalText):
    print("============ BOOKBOT ============")
    print(f"Analysing book found at {address}...")
    print("----------- Word Count ----------")
    print(f"Found {word_counter(originalText)} total words")
    print("--------- Character Count -------")

    for item in charDict:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")
        else:
            continue

    print("============= END ===============")

   # key=lambda item: item['num']