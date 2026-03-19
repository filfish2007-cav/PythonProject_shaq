# # # Модуль 7. Кортежі, множини словники частина 2
# # task 1
# users = list(set(input("Enter your users cherezrez komu: ").split(", ")))
# print(users)
# # task 2
# given_coupons = ["Олексій", "Марія", "Іван", "Олена", "Дмитро"]
# used_coupons = ["Іван", "Дмитро", "Максим", "Світлана"]
# def check_coupons(given, used):
#     given_not_used = list(set(given) - set(used))
#     shahrai = list(set(used) - set(given))
#     print(f"Have coupons but didnt use them: {given_not_used}")
#     print(f"Got a discount without coupons: {shahrai}")
#
#
# check_coupons(given_coupons, used_coupons)

# # # Модуль 7. Кортежі, множини словники частина 3
# # task 1
bank_accounts = {
    "Олексій": 15000.50,
    "Марія": 2800.00,
    "Іван": 0.00,
    "Олена": 43500.75,
    "Дмитро": -150.25  # борг
}

def popovnennya(info):
    """
    Функція для поповнення банківських рахунків користувачів.

    Користувач вводить своє ім'я та суму поповнення.
    - Якщо таке ім'я вже є в словнику, баланс збільшується на введену суму.
    - Якщо імені немає, створюється новий запис з початковим балансом = введеній сумі.
    - Вихід з циклу здійснюється, коли користувач вводить 'END' або порожній рядок.

    :param info: словник, де ключ — ім'я користувача (str),
        значення — баланс рахунку (float або int).
        Приклад: {"Олексій": 15000.50, ...}
    :return: нічого явно не повертає (None), але змінює словник info "на місці".
    """

    # Нескінченний цикл роботи з користувачем, поки він не завершить операцію
    while True:
        # Запитуємо ім'я користувача
        korystuvach = input("Enter your name(type END to end operation): ").strip()

        # Умова виходу з циклу:
        # - якщо введено 'END' (в будь-якому регістрі)
        # - або введено порожній рядок
        if korystuvach.upper() == "END" or not korystuvach:
            print("Thank you for using our bank, the balance has been succesfully updated!")
            break

        # Якщо користувач з таким ім'ям уже є в словнику рахунків
        elif korystuvach.lower().title() in info.keys():

            # Другий цикл — поки не буде введена коректна сума
            while True:
                summa = int(input("Enter desired money transfer: "))

                # Перевірка на некоректну суму:
                # - від'ємна
                # - дорівнює нулю
                # (тут можна додати ще умови, наприклад, перевірку типу)
                if summa < 0 or summa == " " or summa == 0:
                    print("Negative amount")
                    continue
                else:
                    # Якщо сума коректна — додаємо її до балансу існуючого користувача
                    info[korystuvach.lower().title()] += summa
                    # Додатковий self-check (можеш додати при бажанні)
                    # print(f"Updated balance for {korystuvach.lower().title()}: {info[korystuvach.lower().title()]}")
                    break


        # Якщо користувача з таким ім'ям ще немає в словнику
        else:

            # Цикл для введення коректної суми для НОВОГО користувача
            while True:
                summa = int(input("Enter desired money transfer: "))

                # Та ж перевірка на від'ємну / нульову суму
                if summa < 0 or summa == " " or summa == 0:
                    print("Negative amount")
                    continue
                else:
                    # Створюємо новий запис у словнику:
                    # ключ — ім'я, значення — сума як початковий баланс
                    info.update({korystuvach.lower().title(): summa})
                    # self-check для перевірки додавання нового користувача
                    print(f"New user added: {korystuvach.lower().title()} with balance {info[korystuvach.lower().title()]}")
                    break


def withdrawal(info):
    """
        Функція для зняття грошей з банківських рахунків користувачів.

        Користувач вводить своє ім'я та суму зняття.
        - Якщо таке ім'я вже є в словнику, баланс зменшується на введену суму.
        - Якщо імені немає, виводить відповідне повідомлення.
        - Вихід з циклу здійснюється, коли користувач вводить 'END' або порожній рядок.

        :param info: словник, де ключ — ім'я користувача (str),
            значення — баланс рахунку (float або int).
            Приклад: {"Олексій": 15000.50, ...}
        :return: нічого явно не повертає (None), але змінює словник info "на місці".
        """

    # Нескінченний цикл роботи з користувачем, поки він не завершить операцію
    while True:
        # Запитуємо ім'я користувача
        korystuvach = input("Enter your name(type END to end operation): ").strip()

        # Умова виходу з циклу:
        # - якщо введено 'END' (в будь-якому регістрі)
        # - або введено порожній рядок
        if korystuvach.upper() == "END" or not korystuvach:
            print("the balance has been succesfully updated!")
            break

        # Якщо користувач з таким ім'ям уже є в словнику рахунків
        elif korystuvach.lower().title() in info.keys():

            # Другий цикл — поки не буде введена коректна сума
            while True:
                summa = int(input("Enter desired money withdrawal amount: "))

                # Перевірка на некоректну суму:
                # - від'ємна
                # - дорівнює нулю
                # (тут можна додати ще умови, наприклад, перевірку типу)
                if summa < 0 or summa == " " or summa == 0:
                    print("Negative amount")
                    continue
                else:
                    # Якщо сума коректна — віднімаємо від балансу існуючого користувача
                    info[korystuvach.lower().title()] -= summa
                    break

        # Якщо користувача з таким ім'ям ще немає в словнику
        else:
            print("No such user in database")

def main():
    while True:
        choice = input("Enter your choice of operation (withdrawal or transfer) (type END to end operation): ").strip()
        if choice.upper() == "END" or not choice:
            print("Thanks for using our bank")
            break
        elif choice.lower() == "withdrawal":
            withdrawal(bank_accounts)
        elif choice.lower() == "transfer":
            popovnennya(bank_accounts)
    print("Updated list of users in bank check if your operations been done \n {}".format(bank_accounts))

main()


