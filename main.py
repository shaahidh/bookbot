def get_book_text(path):
    try:
        with open(path) as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: File {path} not found.")
        return ""
    
def count_words(file_contents):
    words= file_contents.split()
    return len(words)

def count_characters(file_contents):
    lower = file_contents.lower()
    characters = list(lower)
    letter_dict = {}
    for letter in characters:
        if letter.isalpha():
            if letter in letter_dict:
                letter_dict[letter] += 1            
            else:
                letter_dict[letter] = 1
    return letter_dict


def main():
    book_path = "books/frankenstein.txt"
    #print(file_contents)
    text = get_book_text(book_path)
    #print(f"the count: {count_words(text)}")
    #print(f"number of characters: {count_characters(text)}")
    print("-- Begin report of books/frankenstein.txt --")
    print(f"{count_words(text)} words found in the document")
    letter_dict = count_characters(text)
    
    for key,value in sorted(letter_dict.items()):
        print(f"the '{key}' character was found {value} times")
    print("--- End report ---")
        
main()



