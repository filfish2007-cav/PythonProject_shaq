# # task 1
# height = int(input("Vvedit vysotu trikutnyka: "))
# symbol = str(input("Vvedit symvol trikutnyka: "))
# for i in range(1,height+1):
#     print(symbol * i)
# # task 2
# shirina = int(input("Vvedy shirinu: "))
# vysota = int(input("Vvedy vysota: "))
# s1 = input("Vvedy s1: ")
# s2 = input("Vvedy s2: ")
#
# for i in range(vysota):
#     for j in range(shirina):
#         if (i + j) % 2 == 0:
#             print(s1, end="")
#         else:
#             print(s2, end="")
#     print()
# # task 3
# import random
#
# digits = "0123456789"
# secret = "".join(random.sample(digits, 4))
#
# print("Гра 'Бики та корови'. Вгадай 4-значне число!")
#
# while True:
#     guess = input("Твій варіант: ")
#
#     if guess == secret:
#         print("Перемога! Це було число", secret)
#         break
#
#     bulls = 0
#     cows = 0
#
#     for i in range(4):
#         if guess[i] == secret[i]:
#             bulls += 1
#         elif guess[i] in secret:
#             cows += 1
#
#     print(f"Бики: {bulls}, Корови: {cows}")
# # task 4
#
# n = int(input("Enter a number: "))
# NACHANLOE = n
# length = len(str(n))
# summa = 0
# for i in range(length):
#     cr = n % 10
#     b = 1
#     for j in range(length):
#         b *= cr
#     summa += b
#     n = n // 10
# if summa == NACHANLOE:
#     print(f"This is armstrong number: {summa}")
# else:
#     print(f"Not armstrong number: {summa}")
# # task 5
# vysota = int(input("Enter height "))
# sym = str(input("Enter symbol "))
#
# for i in range(1,vysota+1,2):
#     print(sym*i)
# for i in range(vysota-2,0,-2):
#     print(sym*i)
# # task 6
# vysota = int(input("Введіть висоту ромба (непарне число): "))
# sym = input("Введіть символ: ")
#
# for i in range(1, vysota + 1, 2):
#     spaces_left = (vysota - i) // 2
#     if i == 1:
#         print(" " * spaces_left + sym)
#     else:
#         spaces_inner = i - 2
#         print(" " * spaces_left + sym + " " * spaces_inner + sym)
#
# for i in range(vysota - 2, 0, -2):
#     spaces_left = (vysota - i) // 2
#     if i == 1:
#         print(" " * spaces_left + sym)
#     else:
#         spaces_inner = i - 2
#         print(" " * spaces_left + sym + " " * spaces_inner + sym)
