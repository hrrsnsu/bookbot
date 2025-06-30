def get_book_word_count(text):
    return len(text.split())

def get_character_count(text):
    count_dict = {}
    for char in text:
        lower_char = char.lower()
        if lower_char in count_dict:
            count_dict[lower_char] += 1
        else:
            count_dict[lower_char] = 1
    return count_dict


def get_sorted_char_arr(dict):
    def sort_on(arr): 
        return arr["count"]
    
    dict_arr = []
    for key, value in dict.items():
        dict_arr.append({"char": key, "count": value})
    
    dict_arr.sort(reverse=True, key=sort_on)
    return dict_arr
    