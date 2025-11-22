from stats import get_num_words
from stats import get_num_characters
from stats import char_count


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
    Character_count_list = char_count(letters)


    #Formating
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {relative_file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for dict in Character_count_list:
        char = dict["char"]
        num = dict["num"]
        if char.isalpha():
            print(f"{char}: {num}")
    
    print("============= END ===============")





    #print(letters)
    

    


main()
