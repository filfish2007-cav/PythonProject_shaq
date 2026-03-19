# # task 1
#
# def merge_dicts(dict_a, dict_b):
#
#     result = {}
#
#     for key, value in dict_a.items():
#         result[key] = value
#
#     for key, value in dict_b.items():
#         if key in dict_a.keys():
#
#             result[key] = result[key] + value
#         else:
#
#             result[key] = value
#
#     print(f"Перший словник: {dict_a}")
#     print(f"Другий словник: {dict_b}")
#     return f"Результат обʼєднання: {result}"
#
#
#
# d1 = {"a": 1, "b": 2, "d": 10}
# d2 = {"b": 3, "c": 4, "d": 5}
#
# merged = merge_dicts(d1, d2)
#
# print(f"Кінцевий merged: {merged}")
# # task 2
# slovnik = {'Chocolate': 'Black', 'Banana': 'Green', 'Cheese': 'Dor Blue'}
# def swap(sl):
#     reversed_sl = {}
#     for key, value in sl.items():
#         reversed_sl[value] = key
#     return reversed_sl
# print(swap(slovnik))
# # task 3
# products_prices = {}
# while True:
#     key = input("Nazva productu? ")
#     price_input = input("price? ")
#
#     if key != "" or price_input != "":
#         price = float(price_input)
#
#         if key in products_prices:
#             products_prices[key] += price
#
#         else:
#             products_prices[key] = price
#
#     else:
#         print(products_prices)
#         break
# # task 4
# def func(txt, format = "percentage"):
#     slv = {}
#     words = set(list(txt))
#     words.remove(' ')
#     if format == 'kilkist':
#         for word in words:
#             slv[word] = txt.count(word)
#     elif format == 'percantage':
#         vsego = 0
#         for word in words:
#             vsego += txt.count(word)
#         for word in words:
#             slv[word] = str(round((txt.count(word)/vsego)*100)) + " %"
#     return slv
# print(func("mavpa abama kakama","percantage"))
# # task 5
# slovnik = {}
#
# def dodvannya(slv):
#     while True:
#         nomer = input("Номер групи (або Enter для виходу): ").strip()
#         if not nomer:
#             break
#
#         members_input = input(f"Введіть учасників для групи {nomer} (через пробіл): ").strip().split()
#
#         if nomer in slv:
#
#             slv[nomer].update(members_input)
#         else:
#
#             slv[nomer] = members_input
#     return slv
#
#
# def vidnimanya(slv):
#     nomer = input("З якої групи видалити учасника? ").strip()
#
#     if nomer in slv:
#         member = input("Ім'я учасника для видалення: ").strip()
#         if member in slv[nomer]:
#
#             slv[nomer].remove(member)
#             print(f"Користувача {member} видалено.")
#
#             if not slv[nomer]:
#                 del slv[nomer]
#         else:
#             print("Такого учасника немає в цій групі.")
#     else:
#         print("Групу не знайдено.")
#
#
# def vyvedennya(slv):
#     print("\n" + "=" * 30)
#     print("ПОТОЧНИЙ СКЛАД ГРУП:")
#     if not slv:
#         print("Словник порожній.")
#     for nomer, members in slv.items():
#         print(f"Група №{nomer}: {', '.join(sorted(members))}")
#     print("=" * 30 + "\n")
#
#
# while True:
#     print("1 - Додати/Оновити групу")
#     print("2 - Видалити учасника")
#     print("3 - Вивести всі групи")
#     print("0 - Вихід")
#
#     choice = input("Оберіть дію: ")
#
#     if choice == "1":
#         dodvannya(slovnik)
#     elif choice == "2":
#         vidnimanya(slovnik)
#     elif choice == "3":
#         vyvedennya(slovnik)
#     elif choice == "0":
#         break
#     else:
#         print("Невірний вибір!")
# # task 6
def info():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    position = input("Enter your position: ")
    full_info = dict(name=name, age=age, position=position)
    return full_info

def add():
    slovnik = {}
    for _ in range(5):
        person_data = info()
        key_name = person_data["name"]
        slovnik[key_name] = person_data["name"],person_data["age"],person_data["position"]

    return slovnik
print(add())





