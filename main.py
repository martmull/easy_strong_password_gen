import math
import random


def is_word_valid(word: str) -> bool:
    if len(word) < 2:
        return False
    return True


def format_word(word: str) -> str:
    return word.lower()


def format_password(password: str) -> str:
    return f"{password[0].upper()}{password[1:-1]}0."


def get_words_list() -> list:
    with open("words.txt") as file:
        words = file.readlines()
    return [
        format_word(word=word.rstrip("\n"))
        for word in words
        if is_word_valid(word=word)
    ]


def generate_password(number_of_words: int) -> str:
    password = ""
    actual_number_of_words = 0
    words = get_words_list()
    while actual_number_of_words < number_of_words:
        password += f"{random.choice(words)}-"
        actual_number_of_words += 1
    return format_password(password=password)


def compute_entropy(number_of_words: int) -> int:
    valid_words_number = len(get_words_list())
    return int(math.log(valid_words_number**number_of_words) / math.log(2))


if __name__ == "__main__":
    number_of_words_in_password = 4
    new_password = generate_password(number_of_words=number_of_words_in_password)
    entropy = compute_entropy(number_of_words=number_of_words_in_password)
    print(f"Password: {new_password}")
    print(f"Entropy: {entropy}")
