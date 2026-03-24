import date_utils

check = input("Input a deadline ")
dniv = date_utils.days_before(check)
print(f"Days before deadline: {dniv}")
if dniv < 7:
    print("Its less then a week before deadline")
