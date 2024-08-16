def main():
    text = get_book_text()
    num_words = get_num_words(text)
    print('--- Begin report of books/frankenstein.txt ---')
    print(f'{num_words} words found in the document')
    print_char_count(text)
    print('---End report---')

def get_book_text():
    book_path = 'books/frankenstein.txt'
    with open(book_path) as f:
        return f.read()

def get_num_words(text):
    words = text.split()
    return len(words)

def print_char_count(text):
    char_count = {}
    content = text.lower()
    for char in content:
        if char.isalpha():
            if char in char_count:
                char_count[char] +=1
            else:
                char_count[char] = 1
    
    sorted_char_count = sorted(char_count.items(), key=lambda item: item[1], reverse= True)

    for char, count in sorted_char_count:
        print(f'"{char}":{count}')


main()