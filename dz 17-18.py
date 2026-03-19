# # task 1
# text = input("Введіть текст: ")
#
# temp_text = text.replace("!", ".").replace("?", ".")
#
# sentences = temp_text.split(".")
#
# count = 0
# for s in sentences:
#     if s.strip():
#         count += 1
#
# print(f"Кількість речень: {count}")
# # task 2
# text = input("Введіть рядок: ").lower() р
#
# if text == text[::-1]:
#     print("Це паліндром!")
# else:
#     print("Це не паліндром.")
# # task 3
# text = input("Введіть рядок: ")
# s1 = input("Перший символ: ")
# s2 = input("Другий символ: ")
#
# idx1 = text.find(s1)
# idx2 = text.find(s2)
#
# if idx1 != -1 and idx2 != -1:
#     res = text[:idx1] + text[idx2 + 1:]
#     print(res)
# else:
#     print("Символи не знайдено")
