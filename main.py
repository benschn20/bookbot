def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    count_of_letters = count_letters(text)
    sorted_list_of_chars = dict_to_sorted_list(count_of_letters)
    print(f"--- Begin report of {book_path} ---")
    print(f"There are {num_words} words in this document!")
    print()
    for item in sorted_list_of_chars:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']} character was found {item['num']} times.")

    print("--- End of report ---")


def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()   
    
def sort_on(d):
    return d["num"]

def dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for char in num_chars_dict:
        sorted_list.append({"char": char, "num": num_chars_dict[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def count_letters(text):
    text = text.lower()
    letter_count = {}
    for letter in text:
        if letter not in letter_count:
            letter_count[letter] = 1
        elif letter in letter_count:
            letter_count[letter] += 1
    return letter_count

main()