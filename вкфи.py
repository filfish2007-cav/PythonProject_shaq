# # # HW 33-34!
# # task 1
# def count_digits(func):
#     def wrapper(text):
#         digits = "0123456789"
#         count = 0
#         for char in text:
#             if char in digits:
#                 count += 1
#         print(f"Кількість цифр у тексті: {count}")
#         return func(text)
#
#     return wrapper
#
#
#
# def count_punctuation(func):
#     def wrapper(text):
#         punctuation = ".,!?;:-()\"'"
#         count = 0
#         for char in text:
#             if char in punctuation:
#                 count += 1
#         print(f"Кількість розділових знаків: {count}")
#         return func(text)
#
#     return wrapper
#
#
#
# def count_exclamations(func):
#     def wrapper(text):
#         count = 0
#         for char in text:
#             if char == "!":
#                 count += 1
#         print(f"Кількість знаків оклику: {count}")
#         return func(text)
#
#     return wrapper
#
#
# @count_digits
# @count_punctuation
# @count_exclamations
# def process_text(text):
#     sentences = text.split(". ")
#     fixed_sentences = []
#
#     for s in sentences:
#         if len(s) > 0:
#             new_sentence = s[0].upper() + s[1:]
#             fixed_sentences.append(new_sentence)
#
#     return ". ".join(fixed_sentences)
#
# input_text = "привіт всім. тут є цифри 1 і 2! ви бачили це? неймовірно!!!"
#
# print("--- АНАЛІЗ ТЕКСТУ ---")
# result = process_text(input_text)
# print("\nВідформатований текст:")
# print(result)
# # task 2
# def count_removed_elements(func):
#     def wrapper(numbers):
#         original_count = len(numbers)
#         unique_list = func(numbers)
#         removed_count = original_count - len(unique_list)
#
#         print(f"\n--- Аналіз ---")
#         print(f"Було елементів: {original_count}")
#         print(f"Видалено дублікатів: {removed_count}")
#         return unique_list
#
#     return wrapper
#
#
#
# @count_removed_elements
# def get_unique_elements(numbers):
#     unique = []
#     for x in numbers:
#         if x not in unique:
#             unique.append(x)
#     return unique
#
#
#
# user_input = input("Введіть цілі числа через пробіл: ")
#
#
# numbers_list = [int(x) for x in user_input.split()]
#
#
# result = get_unique_elements(numbers_list)
#
# print("\nСписок унікальних елементів:")
# print(result)
