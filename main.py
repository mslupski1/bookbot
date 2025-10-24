from stats import get_length, count_chars, dict_to_list_and_sort, report_for_print
import sys

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def main():
    arg = sys.argv
    if len(sys.argv) == 1:
        print("Usage: python3 main.py <path_to_book>")
        return sys.exit(1)
    else:
        book = get_book_text(arg[1])
        count = get_length(book)
        chars_count = count_chars(book)
        chars_dict = dict_to_list_and_sort(chars_count)
        char_report = report_for_print(chars_dict)
        return print(f"============ BOOKBOT ============\nAnalyzing book found at {arg[1]}...\n----------- Word Count ----------\nFound {count} total words\n--------- Character Count -------\n{char_report}============= END ===============")

main()