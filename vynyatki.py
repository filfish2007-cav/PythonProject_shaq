# # task 1
# products = {
#     "яблука": 25.50,
#     "банани": 40.00,
#     "сир": 180.00,
#     "хліб": 15.00
# }
# while True:
#     try:
#         index = input("VVedit nazvu: ")
#         print("Product = ", products[index])
#     except KeyError:
#         print("No such product")
#         continue
#     except ValueError:
#         print("Invalid input")
# # task 2
# def ask_age():
#     age = int(input("Enter age "))
#
#     if age < 0:
#         raise ValueError("Invalid age cant be lower than 0")
#     if age > 100:
#         raise ValueError("Invalid age cant be higher than 100")
#
#
#     return age
# try :
#     age = ask_age()
#     print(f"Vik = {age}")
# except ValueError as err:
#     print("Invalid input: ",err)
# # task 3
# Напишіть функцію, яка запитує користувача номер
# телефону та повертає його. Якщо номер не вірний, тобто не
# починається з +038 або в ньому не 11 символів то викликати
# виняток ValueError.
# Написати код try … except який використовує дану
# функцію.
# def ask_nomer():
#     number = input("VVedit nomer ")
#
#     if number[:4] != '+380':
#         raise ValueError("Not Ukranian number")
#
#     if len(number) != 11:
#         raise ValueError("Not correct number")
#
#     return number
#
#
# try:
#     number = ask_nomer()
#     print(f"Your number is {number=}")
#
# except ValueError as err:
#     print("Error:",err)
# # task 4
