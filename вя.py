# # task 1
# def format_as_json(func):
#     def wrapper():
#         data = func()
#         result = "{\n"
#         for key, value in data.items():
#             result += f'  "{key}": "{value}",\n'
#         result += "}"
#         return result
#     return wrapper
#
# def format_as_tax_report(func):
#     def wrapper():
#         data = func()
#         result = f"--- ЗВІТ ДЛЯ ПОДАТКОВОЇ ---\nКомпанія: {data['company']}\nСума: {data['amount']} грн."
#         return result
#     return wrapper
#
#
# @format_as_json
# def get_report_data():
#     return {"company": "IT-Step", "amount": 50000}
#
# @format_as_tax_report
# def get_report_data():
#     return {"company": "IT-Step", "amount": 50000}
#
# print(get_report_data())
# # task 2
# def audit_decorator(func):
#     def wrapper(user_name, action_data):
#         print(f"ЛОГ: Користувач {user_name} робить дію {func.__name__} з даними: {action_data}")
#         return func(user_name, action_data)
#     return wrapper
#
# @audit_decorator
# def delete_item(user, item_id):
#     return f"Об'єкт {item_id} видалено."
#
# @audit_decorator
# def create_item(user, name):
#     return f"Об'єкт {name} створено."
#
# print(delete_item("Адмін_Олег", 101))
# print(create_item("Admin Dima", 105))
# # task 3
# attempts_counter = {}
#
#
# def rate_limit_decorator(func):
#     def wrapper(user):
#
#         if user not in attempts_counter:
#             attempts_counter[user] = 0
#
#         if attempts_counter[user] >= 3:
#             return f"ДОСТУП ЗАБОРОНЕНО для {user}: забагато запитів!"
#
#         attempts_counter[user] += 1
#         return func(user)
#
#     return wrapper
#
#
# @rate_limit_decorator
# def get_secret_info(user):
#     return f"Таємні дані для {user} завантажено."
#
# print(get_secret_info("Ivan"))
# print(get_secret_info("Ivan"))
# print(get_secret_info("Ivan"))
# print(get_secret_info("Ivan"))
