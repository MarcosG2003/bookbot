def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents


def word_count(text_from_book):
    words = text_from_book.split()
    num_of_words = len(words)
    return num_of_words



def main():
    relative_file_path = "books/frankenstein.txt"
    #print(get_book_text(relative_file_path))
    text = get_book_text(relative_file_path)
    num_words = word_count(text)
    print(f"Found {num_words} total words")
    


main()
