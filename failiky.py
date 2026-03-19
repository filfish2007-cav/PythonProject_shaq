# # Завдання 1
# # Є текстовий файл. Виведіть кількість рядків та кількість символів в ньому

# with open("textik.txt","r") as f:
#     text = f.read()

# with open("resultat","w") as f:
#     dlin = len(text)
#     print(f"Kilkist symbols: {dlin}", file=f)
#     dlin2 = text.count("\n") + 1
#     print(f"Kilkist ryadkiv: {dlin2}", file=f)

# # Завдання 2
# # Користувач вводить ім’я та вік. Запишіть їх у файл. Назву
# # файлу також вводить користувач(без розширення .txt)

# name = input("Enter your name: ")
# age = input("Enter your age: ")
# file_name = input("Enter your file name: ")
# def func(imya,vik,file):
#     file = file + ".txt"
#     with open(f"{file}",'w',encoding='utf-8') as f:
#         print(f"{imya} is {vik} years old", file=f)
# func(name,age,file_name)

# # Завдання 3
# # Є текстовий файл. Запишіть його рядки в інший файл.

# with open('textik.txt', 'r') as f:
#     text = f.readlines()

# with open('resultik.txt', 'w') as f:
#     for line in text:
#         print(line, file=f)

# # Завдання 4
# # Користувач вводить літеру та назву файлу. Виведіть усі
# # слова з файлу, які починаються на цю літеру.

# """
# ПРОЄКТ: Фільтратор слів за першою літерою
# ПРИЗНАЧЕННЯ: Зчитування текстового файлу та збереження слів, що починаються на вказану літеру.
# """
#
# # --- БЛОК ВВОДУ ДАНИХ ---
# # Користувач вводить літеру, за якою буде здійснюватися пошук
# letter = input("Enter a letter: ")
#
# # Користувач вводить назву файлу. Програма автоматично додає розширення .txt
# file_name = input("Enter a file name: ") + ".txt"
#
#
# # --- ОПИС ФУНКЦІЙ ---
#
# def read_file(failik):
#     """
#     Зчитує вміст файлу та розбиває його на список слів.
#     Параметр failik: назва або шлях до файлу.
#     Повертає: список (list) слів, розділених пробілом.
#     """
#     with open(failik, "r", encoding="utf-8") as f:
#         # Зчитуємо весь текст у змінну orig
#         orig = f.read()
#     # Розбиваємо текст на окремі елементи списку за пробілом
#     orig = orig.split(" ")
#     return orig
#
#
# def output_words(bukva):
#     """
#     Отримує список слів, фільтрує їх за першою літерою та записує результат у новий файл.
#     Параметр bukva: літера для порівняння.
#     """
#     # Викликаємо функцію read_file для отримання списку слів з вхідного файлу
#     slova = read_file(file_name)
#
#     # Відкриваємо (або створюємо) файл 'slova.txt' для запису ("w")
#     with open("slova.txt", "w", encoding="utf-8") as f:
#         for word in slova:
#             # 1. strip() прибирає зайві знаки пунктуації навколо слова
#             # 2. lower() переводить слово в нижній регістр для коректного порівняння
#             # 3. startswith() перевіряє, чи починається слово на задану літеру
#             if word.strip(".,!?;:()\"").lower().startswith(bukva):
#                 # Записуємо слово у файл (print з параметром file автоматично додає перенос рядка)
#                 print(word, file=f)
#
#
# # --- БЛОК ВИКОНАННЯ ---
#
# try:
#     # Запускаємо головну функцію обробки
#     output_words(letter)
#     print("Success! Check 'slova.txt' for results.")
# except FileNotFoundError:
#     # Виводиться повідомлення, якщо вказаний користувачем файл не існує в папці
#     print("Nema takogo failu")

# # Завдання 5
# # Є текстовий файл. Замініть у ньому усі символи * на &, та навпаки.

# with open("textik.txt","r", encoding = 'utf-8') as f:
#     outputik = f.read()
#
#     temp_text = outputik.replace("*","#")
#     temp_text = temp_text.replace("&","*")
#     final_text = temp_text.replace("#","&")
#
# with open("resultik.txt","w",encoding = 'utf-8') as f:
#     f.write(final_text)

# # Завдання 6
# # Напишіть функцію, яка отримує назву файлу та список
# # чисел як параметри. Потрібно записати всі числа у файл,
# # розмістивши кожне число на окремому рядку.
# # Напишіть іншу функцію, яка отримує назву файл та читає
# # з нього ці числа і повертає як список.
# file_name = input("Enter file name: ") + ".txt"
# chisla = input("Enter chisla cherez komu: ").split(" ")
#
# def zapis(file,nums):
#     with open(file,"w",encoding="utf-8") as f:
#         for num in nums:
#             print(num,end="\n",file=f)
#
# def perevod(file):
#     zapis(file_name, chisla)
#
#     with open(file,"r",encoding="utf-8") as f:
#         text = f.read()
#
#     chisla2 = []
#
#     for num in text:
#
#         if num != "\n":
#             chisla2.append(num)
#
#     return chisla2
# print(perevod(file_name))
# # Завдання 7
# # Є 2 файли, запишіть у третій файл лише ті символи, які є в
# # обох файлах одночасно
# filek1 = input("vvedy text dlya first file: ")
# filek2 = input("vvedy text dlya second file: ")
#
# def create_file():
#     with open("numba1.txt", "w", encoding="utf-8") as f:
#         print(f"{filek1}", file=f)
#
#     with open("numba1.txt", "r", encoding="utf-8") as f:
#         text1 = f.read()
#     text1 = set(text1)
#
#     with open("numba2.txt", "w", encoding="utf-8") as f:
#         print(f"{filek2}", file=f)
#
#     with open("numba2.txt", "r", encoding="utf-8") as f:
#         text2 = f.read()
#     text2 = set(text2)
#
#     common = text1 & text2
#     common.remove("\n")
#
#     return common
#
# def write_common():
#     with open("numba3.txt", "w", encoding="utf-8") as f:
#         print(f"{create_file()}", file=f)
#
#     with open("numba3.txt", "r", encoding="utf-8") as f:
#         text3 = f.read()
#
#     return text3
#
# print(write_common())
# # Завдання 8
# # There is a file with text. Remove all unacceptable words from it.
# # The list of unacceptable words is in another file.
# bad_words = input("Input not acceptable words with spacces ").split()
#
# def create_bad_words():
#     with open("bad_words.txt", "w", encoding="utf-8") as f:
#         for word in bad_words:
#             print(f"{word}", file=f)
#
#     with open("bad_words.txt", "r", encoding="utf-8") as f:
#         text = f.readlines()
#         textf = []
#         for line in text:
#             textf.append(line.lower().strip("\n"))
#     return textf
#
#
#
# def remove_bad_words(to_delete):
#     with open("textik.txt", "r", encoding="utf-8") as f:
#         text = f.read()
#     text1 = text.lower()
#     words = text1.split(" ")
#     new_words = []
#     for word in words:
#         if word not in to_delete:
#             new_words.append(word)
#
#     new_text = " ".join(new_words)
#
#
#     with open("textik.txt", "w", encoding="utf-8") as f:
#         f.write(new_text)
#
#     return new_text
#
# deletables = create_bad_words()
# print(remove_bad_words(deletables))



text_file = input("Please enter the file text: ")
def file1(textik):
    with open("random.txt", "w",encoding="utf-8") as f:
        f.write(textik)
    with open("random.txt", "r",encoding="utf-8") as f:
        text = f.read()

    return text
def file2(textik):
    with open("random_stat.txt", "w",encoding="utf-8") as f:
        length = len(textik)
        ryadki = textik.count("\n") + 1
        chisla = 0
        golosni = ["a","e","u","i","o"]
        golosni_kil = 0
        for i in textik:
            if i.isdigit():
                chisla += 1
            elif i in golosni:
                golosni_kil += 1
    return f"there are {ryadki} lines, there are {chisla} chisel, there are {golosni_kil} golosnyh"
textf = file1(text_file)
print(file2(textf))




















