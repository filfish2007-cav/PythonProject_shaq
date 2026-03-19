# task 1
# kvadrat = lambda num: num + 10
# perymert = lambda s1, s2, s3: s1+s2+s3
# imya = lambda name, surname: f"{surname.title()}, {name.title()}"
# parne = lambda num: num % 2 == 0
# task 2
def pos_nums(numbers):
    return list(filter(lambda x: x > 0, numbers))

data = [-10, 5, 0, 3, -2, 8]
result = pos_nums(data)
print(result)

def three_mo(slova):
    return list(filter(lambda x: len(x)>3, slova))

slovechki = ["Adolf","jew"]
result = three_mo(slovechki)
print(result)

def poch_na(slova):
    def filter_by_letter(words, letter):
        target = letter.lower()
        return list(filter(lambda word: word.lower().startswith(target), words))

    word_list = ["Apple", "banana", "Apricot", "cherry", "avocado"]
    search_char = "a"

    result = filter_by_letter(word_list, search_char)
    print(result)