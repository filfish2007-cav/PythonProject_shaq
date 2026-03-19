# # task 1
# def get_password():
#     password = input("Input your password: " )
#
#     for i in password:
#
#         if password.count(i) > 1:
#             raise ValueError("Invalid password")
#
#     if len(password) < 8:
#         raise ValueError("Invalid password")
#
#     return password
#
#
# def main():
#     while True:
#         try:
#             parol = get_password()
#             print(parol)
#
#         except ValueError as e:
#             print(e)
#             continue
#
#         break
#
# main()
# # task 2
users_db = {
    "admin": "admin1234",
    "pasha_python": "qwerty2024",
    "olena_dev": "securePass77",
    "guest": "12345"
}

def login_password():
    login = input("input your login: ")

    if login not in users_db:
        raise KeyError("Incorrect login")

    password = input("input your password: ")

    if password not in users_db.values():
        raise ValueError("Incorrect password")

    else:
        print("Access granted")


while True:
    try:
        login_password()

    except KeyError as e:
        print(e)
        continue

    except ValueError as e:
        print(e)
        continue
    break
