

def print_book():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
    return file_contents

def wordCounter(text):
    return len(text.split())

def count_characters(text):
    character_count = {}
    text = text.lower()  
    for char in text:
        if char.isalpha():
            if char in character_count:
                character_count[char] += 1
            else:
                character_count[char] = 1
    return character_count

def sortingFunction(item):
    return item[1]

def report(character_count, text):
     print("--- Begin report of books/frankenstein.txt ---")
     print(f"{wordCounter(text)} words found in the document")
    
     sorted_chars = sorted(character_count.items(), key=sortingFunction, reverse=True)

    
     for char, count in sorted_chars:
        print(f"The '{char}' character was found {count} times")
    
     print("--- End report ---")


def main():
    text = print_book()
    wordCount = wordCounter(text)
    charCount = count_characters(text)
    
    print(report(charCount, text))

main()

