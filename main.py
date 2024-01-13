from collections import defaultdict
def main():
    with open('books/frankenstein.txt') as file:
        book = file.read()
    word_count = len(book.split())
    char_counts = defaultdict(int)

    for char in book:
        char_counts[char.lower()] += 1

    print('--- Begin report of books/frankenstein.txt ---')
    print(f'{word_count} words found in the document')
    for char, count in sorted(list(char_counts.items()), key=lambda x: x[1], reverse=True):
        if not char.isalpha():
            continue
        print(f"The '{char}' character was found {count} times")

if __name__ == '__main__':
    main()