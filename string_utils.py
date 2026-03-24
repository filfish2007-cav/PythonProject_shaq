def remove_punctuation(text):
    punctuation = ",.?!;:"
    table = str.maketrans("", "", punctuation)
    return text.translate(table)


def count_vowels(text):
    vowels = "aeiouyAEIOUYаеєиіїоуюяАЕЄИІЇОУЮЯ"
    return sum(1 for char in text if char in vowels)


def is_palindrome(text):
    clean_text = "".join(text.split()).lower()
    return clean_text == clean_text[::-1]
