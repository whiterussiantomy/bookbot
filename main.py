def main():
    with open("books/frankestein.txt") as f:
        file_contents = f.read()
        no_words = count_words(file_contents)
        print(no_words)    

def count_words(content):
    return len(content.split())

main()