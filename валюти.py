# # task 1
# rates = {
#     "UAH": 1.0,    # 1 гривня коштує 1 гривню
#     "USD": 38.50,  # курс долара до гривні
#     "EUR": 41.20,  # курс євро до гривні
#     "PLN": 9.60,   # курс злотого до гривні
#     "GBP": 48.10   # курс фунта до гривні
# }
#
# def get_currency():
#     valuta = input("Which currency are you interested in? ")
#
#     if valuta.upper() in rates:
#         return valuta.upper()
#
#     else:
#         raise ValueError("enter a valid currency(UAH, USD, EUR, PLN, GBP)")
#
#
# def get_amount():
#     while True:
#         amount = input("Which sum do u want to convert? ")
#
#         if amount.isdigit() and float(amount) > 0 :
#             return float(amount)
#
#         else:
#             raise ValueError("enter a valid amount greater than 0 and it should be a number")
#
#
# def get_convert():
#     converting = input("Which currency are you interested to convert to? ")
#
#
#     if converting.strip().upper() in rates:
#         return converting.upper()
#
#     else:
#         raise ValueError("enter a valid currency(UAH, USD, EUR, PLN, GBP)")
#
# def main():
#     while True:
#         try:
#             currency = get_currency()
#             print(currency)
#         except ValueError as e:
#             print("Error: {}".format(e))
#             continue
#         break
#     while True:
#         try:
#             summa = get_amount()
#             print(summa)
#         except ValueError as e:
#             print("Error: {}".format(e))
#             continue
#         break
#     while True:
#         try:
#             convert = get_convert()
#             print(convert)
#         except ValueError as e:
#             print("Error: {}".format(e))
#             continue
#         break
#     result = summa * rates[currency] / rates[convert]
#     print( f"{summa} {currency} in {convert} is {result} ")
# # task 2
# Множини з іменами працівників
office_workers = {"Олександр", "Марія", "Іван", "Наталія", "Дмитро"}
remote_workers = {"Іван", "Олена", "Дмитро", "Сергій", "Анна"}
vsi = office_workers | remote_workers
both = office_workers & remote_workers
vidsotok = (len(both) / len(vsi)) * 100
print(f"all workers: {vsi} \n office and remote workers: {both} vidsotok: {vidsotok}")
