# import random
# ls = random.randint(-10, 10)
# print(ls)
# summa_pos = 0
# for i in ls:
#     if i > 0:
#         summa_pos += i
# summa_neg = 0
# for i in ls:
#     if i < 0:
#         summa_neg += i
# summa_even = 0
# for i in ls:
#     if i % 2 == 0:
#         summa_even += i
# summa_odd = 0
# for i in ls:
#     if i % 2 != 0:
#         summa_even += i
# for z, v in enumerate(ls):
#     print(z, v)
#
# print(summa_even)
# print(summa_odd)
# print(summa_neg)
# # task 1
# def get_product_in_range(a, b):
#     if a > b:
#         a, b = b, a
#
#     product = 1
#     for num in range(a, b + 1):
#         product *= num
#
#     return product
# # task 2
# def find_maximum(numbers):
#     if not numbers:
#         return None
#
#     max_value = numbers[0]
#
#     for num in numbers:
#         if num > max_value:
#             max_value = num
#
#     return max_value
# task 3
# def calculate_sum_recursive(numbers):
#     if not numbers:
#         return 0
#     return numbers[0] + calculate_sum_recursive(numbers[1:])

raw_input = input("Введіть цілі числа через пробіл: ")
# Перетворюємо рядок у список цілих чисел
numbers = [int(x) for x in raw_input.split()]

# 2. Ініціалізація лічильників
even_count = 0
odd_count = 0

# 3. Обхід списку та підрахунок
for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

# 4. Виведення результатів
print("Результати:")
print("Парних чисел:", even_count)
print("Непарних чисел:", odd_count)
