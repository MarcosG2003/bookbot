def get_num_words(text_from_book):
    words = text_from_book.split()
    num_of_words = len(words)
    return num_of_words

#Add a new function
#that takes the text from the book as a string
#and returns the number of times each character (including sysmbols and spaces)
#appears in the string
#Convert any character to lowercase using .lower() method
#Use a dictionary of String -> Integer.
#should look like this 
#{'p': 6121, 'r': 20818, 'o': 25225, ...

def get_num_characters(text_from_book):
    text = text_from_book.lower()
    
    letter_count_dict = {}
    

    for char in text:
        if char in letter_count_dict:
            letter_count_dict[char] += 1
        else:
            letter_count_dict[char] = 1
    return letter_count_dict


