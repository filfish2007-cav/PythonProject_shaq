# # task 1

# func_1 = lambda x: x*-1
# print(func_1(3))

# func_2 = lambda x: bool(x)
# print(func_2("gol"))

# # task 2

# chs = list(map(int, input("Vved chisla cherez probil ").split(" ")))

# if chs != "":# отримання списку чисел з сирого інпуту
#     bilshe_ser = list(filter(lambda x: x>sum(chs)/len(chs),  chs)) # створення списку чисел які більше середнього арифметичного
#     nova = list(set(bilshe_ser))
#     print(nova)
# else:
#     print("What the fuck man")
#
# slv = input("Vved slova cherez probil ").split(" ") # отримання слів з сирого інпуту

# if slv != "":
# litery_4 = list(filter(lambda x: len(x) == 4,  slv))
# print(litery_4)

# # task 3
# def find_word_with_max_letter(letter, word_list):
#
#     if not word_list:
#         return None
#
#     result = max(word_list, key=lambda word: word.lower().count(letter.lower()))
#
#     if result.lower().count(letter.lower()) == 0:
#         return "Буква не найдена ни в одном слове"
#
#     return result
#
#
# words = ["яблоко", "ананас", "банан", "арбуз"]
# target_letter = "а"



