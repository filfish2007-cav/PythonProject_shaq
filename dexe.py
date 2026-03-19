# # task 1
# def print_quote():
#     line1 = "\"Don't compare yourself with anyone in this world… "
#     line2 = "    if you do so, you are insulting yourself.\""
#     line3 = "        Bill Gates"
#
#     print(line1)
#     print(line2)
#     print(line3)
#
#
# print_quote()
# # task 2
# def print_even_numbers(start, end):
#     if start > end:
#         start, end = end, start
#
#     for num in range(start, end + 1):
#         if num % 2 == 0:
#             print(num, end=" ")
#     print()
#
# print_even_numbers(2, 11)
# # task 3
# def draw_square(side, symbol, is_filled):
#     if side <= 0:
#         return
#
#     for i in range(side):
#         if is_filled:
#             print(symbol * side)
#         else:
#             if i == 0 or i == side - 1:
#                 print(symbol * side)
#             else:
#                 spaces = " " * (side - 2)
#                 print(symbol + spaces + symbol)
#
#
# print("Заповнений квадрат (4, '*', True):")
# draw_square(4, "*", True)
#
# print("\nПорожній квадрат (5, '#', False):")
# draw_square(5, "#", False)
# # task 4
# def chisla(num1,num2,num3,num4,num5):
#     print(min(num1,num2,num3,num4,num5))
#     print(max(num1,num2,num3,num4,num5))
# chisla(9,20,13,5,4)
# # task 5
# def kilchisel(chislo):
#     return len(str(abs(chislo)))
# result = kilchisel(34517376)
# print(result)
# # task 6
def is_palindrome(number):
    s = str(number)
    return s == s[::-1]

print(is_palindrome(123321))  # True
print(is_palindrome(421987))  # False