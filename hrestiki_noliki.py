# # Поле гри:
# grid = [
#     [" ", " ", " "],
#     [" ", " ", " "],
#     [" ", " ", " "]
# ]
#
#
# def print_grid():
#     """
#     Виводить ігрове поле у консоль
#     """
#     for i in range(3):
#         # символи у рядку
#         print(grid[i][0] + " | " + grid[i][1] + " | " + grid[i][2])
#         # Після першого та другого рядка малюємо горизонтальну лінію
#         if i < 2:
#             print("---------")
#
#
# def check_winner():
#     """
#     Перевіряє, чи є на полі три однакові символи в ряд, стовпчик або діагональ.
#
#     Повертає:
#         "X" або "O", якщо є переможець.
#         None (нічого), якщо переможця поки немає.
#     """
#     # Перевірка всіх рядків
#     for i in range(3):
#         if grid[i][0] == grid[i][1] == grid[i][2] and grid[i][0] != " ":
#             return grid[i][0]
#
#     # Перевірка всіх стовпчиків
#     for i in range(3):
#         if grid[0][i] == grid[1][i] == grid[2][i] and grid[0][i] != " ":
#             return grid[0][i]
#
#     # Перевірка головної діагоналі
#     if grid[0][0] == grid[1][1] == grid[2][2] and grid[0][0] != " ":
#         return grid[0][0]
#
#     # Перевірка побічної діагоналі
#     if grid[0][2] == grid[1][1] == grid[2][0] and grid[0][2] != " ":
#         return grid[0][2]
#
#     return None
#
#
# def is_board_full():
#     """
#     Перевіряє, чи залишилися на полі вільні місця.
#
#     Повертає:
#         True, якщо всі клітинки зайняті.
#         False, якщо є хоча б один пробіл " ".
#     """
#     for row in grid:
#         for cell in row:
#             if cell == " ":
#                 return False
#     return True
#
#
# # Початок ігрового процесу
#
# # Змінна для відстеження того, чий зараз хід
# current_player = "X"
#
# while True:
#     print_grid()
#     print("Хід гравця:", current_player)
#
#     # Запит координат
#     row = int(input("Рядок (0, 1, 2): "))
#     col = int(input("Стовпчик (0, 1, 2): "))
#
#     # Перевірка
#     if 0 <= row <= 2 and 0 <= col <= 2 and grid[row][col] == " ":
#         # Ставимо символ гравця
#         grid[row][col] = current_player
#
#         # Перевірка чи цей хід приніс перемогу?
#         winner = check_winner()
#         if winner:
#             print_grid()
#             print("Переміг", winner)
#             break
#
#         # Перевірка: чи не закінчилися місця
#         if is_board_full():
#             print_grid()
#             print("Нічия!")
#             break
#
#         # Зміна гравця
#         if current_player == "X":
#             current_player = "O"
#         else:
#             current_player = "X"
#     else:
#         print("Помилка: невірні координати або клітинка вже зайнята!")
