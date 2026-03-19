# # task 1

# text_file = input("Please enter the file text: ")

# def file1(textik):
#     with open("random.txt", "w",encoding="utf-8") as f:
#         f.write(textik)

#     with open("random.txt", "r",encoding="utf-8") as f:
#         text = f.read()
#
#     return text
# def file2(textik):
#     with open("random_stat.txt", "w",encoding="utf-8") as f:
#         length = len(textik)
#         ryadki = textik.count("\n") + 1
#         chisla = 0
#         golosni = ["a","e","u","i","o"]
#         golosni_kil = 0

#         for i in textik:
#             if i.isdigit():
#                 chisla += 1

#             elif i.lower() in golosni:
#                 golosni_kil += 1

#     return f"there are {ryadki} lines, there are {chisla} chisel, there are {golosni_kil} golosnyh"

# textf = file1(text_file)
# print(file2(textf))

# # task 2

# slovo = input("Please enter the file key word: ").lower()
# file_name = input("Please enter the file name: ")

# try:
#     with open(file_name, "r",encoding="utf-8") as f:
#         text = f.read()
#         text = text.lower()

#     with open("stats.txt", "w", encoding="utf-8") as f:
#         print(f"{text.count(slovo)} times this word appear in file", file=f)

# except FileNotFoundError:
#     print(f"{file_name} does not exist")

# # task 3

# with open("textik.txt","r", encoding = "utf-8") as f:
#     text = f.readlines()

# with open("textik.txt","w", encoding = "utf-8") as f:
#     for line in range(len(text)-1):
#         f.write(text[line])
