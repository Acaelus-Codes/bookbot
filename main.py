def main():

    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
    
    char_counts = count_characters(file_contents.lower())
    word_count = num_words(file_contents)

    print("--- Generating Your Book Report! ---")
    print(f"There are a whopping {word_count} words in this book!")
    print("Here are all the alphabetical characters in the book: ")
    for char, count in sorted(char_counts.items()):
        print(f"{char}: {count}")
    print("--- Report Completed! ---")


def num_words(book):
    words = book.split()
    return len(words)

def count_characters(text):

    character_count = {}

    for char in text:
        if char.isalpha():
            if char in character_count:
                character_count[char] += 1
            else:
                character_count[char] = 1

    return character_count

    

if __name__ == "__main__":
    main()


