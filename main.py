def main():
    book_name = "books/frankestein.txt"
    file_contents = get_contents(book_name)
    no_words = count_words(file_contents)
    chars_dict = count_letters(file_contents)
    print_report(book_name, no_words, chars_dict)

def get_contents(book_name):
    with open(book_name) as f:
        return f.read()
    

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


def print_report(book_name, total_words, dic):
    ls = []
    for k in dic:
        if k.isalpha():
            ls.append({"char": k, "num": dic[k]})
    ls.sort(reverse = True, key = lambda d: d["num"])
    
    print(f"--- Begin report of {book_name} ---")
    print(f"{total_words} words found in the document")
    print()
    for dic in ls:
        print(f"The '{dic["char"]}' character was found {dic["num"]} times")
    print("--- End report ---")


main()