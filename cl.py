# # task 1
# def sum_digits(n):
#     if n < 10:
#         return n
#     else:
#         return (n % 10) + sum_digits(n // 10)
#
#
# number = int(input("Введіть число: "))
# print(f"Сума цифр числа {number}: {sum_digits(number)}")
# # task 2
# def perevirka(data):
#     if data == data[::-1]:
#         print("Палиндром ")
#     else:
#         print("Не палиндром")
# my_list = [1, 2, 3, 2, 1]
# perevirka(my_list)
# # task 3
# import random
#
# def generate_number():
#     digits = list(range(10))
#     random.shuffle(digits)
#     return ''.join(map(str, digits[:4]))
#
#
# def play_round(secret, attempts=1):
#     guess = input(f"Спроба №{attempts}. Введіть 4 цифри: ")
#
#     if len(guess) != 4 or not guess.isdigit():
#         print("Помилка: потрібно ввести саме 4 цифри.")
#         return play_round(secret, attempts)
#
#     cows = sum(1 for i in range(4) if guess[i] == secret[i])
#     bulls = sum(1 for char in guess if char in secret)
#
#     print(f"Бики (всього вгадано): {bulls}, Корови (на своїх місцях): {cows}")
#
#     if cows == 4:
#         print(f"Вітаю! Ви вгадали число {secret} за {attempts} спроб.")
#         return attempts
#     else:
#         return play_round(secret, attempts + 1)
#
#
# if __name__ == "__main__":
#     secret_number = generate_number()
#     print("Гру розпочато! Загадано 4-цифрове число з унікальними цифрами.")
#     play_round(secret_number)
