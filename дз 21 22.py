# # task 1
# text = input("Введіть текст: ")
# symbols = input("Введіть символи для видалення: ")
#
# words = text.split()
# result = []
#
# for word in words:
#     has_symbol = False
#     for s in symbols:
#         if s in word:
#             has_symbol = True
#             break
#
#     if not has_symbol:
#         result.append(word)
#
# print("Результат:", " ".join(result))
# # task 2
# text = input("Введіть текст: ")
# words = text.split()
# reversed_words = words[::-1]
# result = " ".join(reversed_words)
# print("Результат:", result)
# # task 3
# ident = input("Введіть ідентифікатор: ")
# if 1 <= len(ident) <= 20:
#     first = ident[0]
#     if (first.isalpha() and first.isascii()) or first == "_":
#         is_valid = True
#         for char in ident:
#             if not ((char.isalnum() and char.isascii()) or char == "_"):
#                 is_valid = False
#                 break
#
#         if is_valid:
#             print("OK")
#         else:
#             print("NO")
#     else:
#         print("NO")
# else:
#     print("NO")
