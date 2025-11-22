def get_num_words(text_from_book):
    words = text_from_book.split()
    num_of_words = len(words)
    return num_of_words



def get_num_characters(text_from_book):
    text = text_from_book.lower()
    
    letter_count_dict = {}
    

    for char in text:
        if char in letter_count_dict:
            letter_count_dict[char] += 1
        else:
            letter_count_dict[char] = 1
    return letter_count_dict


def sort_on(items):
    return items["num"]


def char_count(numbers_of_letter_dict):

    sorted_list = []


    for char, num in numbers_of_letter_dict.items():
        new_dict = {
            "char" : char,
            "num" : num
         }
        sorted_list.append(new_dict)
    sorted_list.sort(key=sort_on, reverse=True)

    return sorted_list


