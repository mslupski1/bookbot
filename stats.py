def get_length(string):
    word_list = string.split()
    length = len(word_list)
    return length

def count_chars(string):
    string = string.lower()
    chars_list = []
    chars_count = {}
    for x in string:
        if x in chars_list:
            continue
        else:
            chars_list.append(x)
    for x in chars_list:
        count = 0
        for i in string:
            if i == x:
                count += 1
        chars_count[x] = count
    return chars_count

def sort_on(items):
    return items['num']

def dict_to_list_and_sort(dictionary):
    list_of_dicts = []
    for char in dictionary:
        if char.isalpha() == True:
            char_dict = {"char": char, "num": dictionary[char]}
            list_of_dicts.append(char_dict)
    list_of_dicts.sort(reverse=True, key=sort_on)
    return list_of_dicts

def report_for_print(list_of_dicts):
    string = ""
    for x in list_of_dicts:
        list_of_values=[]
        for k,v in x.items():
            list_of_values.append(v)
        string += f"{list_of_values[0]}: {list_of_values[1]}\n"
    return string

