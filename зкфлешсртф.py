# # task 1
# names = set()
#
# while True:
#     name = input("Введіть ім'я (або залиште порожнім для завершення): ").strip()
#
#     if not name:
#         break
#
#     if name in names:
#         print(f"Помилка: ім'я '{name}' вже є у списку.")
#     else:
#         names.add(name)
#
# print(f"\nКількість унікальних людей: {len(names)}")
# # task 2
# all_students = ["Олексій", "Марія", "Іван", "Дарина", "Павло", "Олена", "Максим"]
#
# group_1 = ["Олексій", "Марія", "Іван", "Павло"]
# group_2 = ["Дарина", "Павло", "Олена"]
#
#
# def check_students_2_groups(everyone, g1, g2):
#     all_set = set(everyone)
#     s1, s2 = set(g1), set(g2)
#
#     duplicates = s1 & s2
#
#     missing = all_set - (s1 | s2)
#
#     if duplicates:
#         print(f"Студенти у двох групах одночасно: {duplicates}")
#
#     if missing:
#         print(f"Забуті студенти: {missing}")
# # task 3

# 1. Наш асортимент товарів (ціна за 1 кг)
products = {
    "яблука": 25.50,
    "банани": 40.00,
    "сир": 180.00,
    "хліб": 15.00
}


item = input("Введіть назву продукту: ").lower().strip()

if item in products:
    weight = float(input(f"Введіть вагу для '{item}' (у кг): "))

    total_price = products[item] * weight

    print("-" * 20)
    print(f"Вартість покупки: {total_price} грн")
else:
    print("На жаль, такого продукту немає в асортименті.")
