
def main():
    filename = input('Enter the name of the input file: ')

    try:
        input_file = open(filename, 'r')
        text = input_file.read()
        input_file.close()
    except FileNotFoundError:
        print('The file was not found.')
        return

    words = text.split()
    unique_words = set(words)
    counts = {}

    for word in unique_words:
        counts[word] = words.count(word)

    print('Word'.ljust(20) + 'Occurrences')
    print('-' * 43)
    for word in sorted(counts):
        print(word.ljust(20) + str(counts[word]))


if __name__ == '__main__':
    main()
