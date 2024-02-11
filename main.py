def main():
    with open("books/frankestein.txt") as f:
        file_contents = f.read()
        no_words = count_words(file_contents)
        print(no_words) 

        chars_dict = count_letters(file_contents)
        print(chars_dict)

def count_words(content):
    return len(content.split())

def count_letters(text):
    chars = {}
    for c in text.lower():
        if c not in chars:
            chars[c] = 1
        else:
            chars[c] += 1
    return chars

main()