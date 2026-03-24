# # task 1
# import math
#
# def temp(T_env = 5,T0 = 95,t = 60,k = 0.05):
#     T_new = T_env + (T0-T_env) *math.exp(-k*t)
#     return T_new
# print(temp())
# # task 2
# import time
# def func(show_time = False):
#     start_time = time.time()
#     name = input("Whats ur name ")
#     print(name)
#     end_time = time.time()
#     if show_time == True:
#         print(end_time - start_time)
# func(True)
