from stats import get_num_words
from stats import get_num_characters


def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents



def main():
    relative_file_path = "books/frankenstein.txt"
    #print(get_book_text(relative_file_path))
    text = get_book_text(relative_file_path)
    num_words = get_num_words(text)
    letters = get_num_characters(text)



    print(f"Found {num_words} total words")
    print(letters)

    


main()
