# # task 1
# c1 = (3,8,5,18,43,2,8)
# c2 = (0,1,2,3,4,5,6,7,8,9)
# c3 = (8,3,13,69,67,34,41)
# common = []
# for i in c1:
#     if i in c2 and i in c3 and i not in common:
#         common.append(i)
#
# print(common)
# # task 2
# c1 = (3,8,5,18,43,2,8)
# c2 = (0,1,2,3,4,5,6,7,8,9)
# c3 = (8,3,13,69,67,34,41)
# s1, s2, s3 = set(c1), set(c2), set(c3)
# unique1 = s1 - s2- s3
# print(unique1)
# unique2 = s2 - s1 - s3
# print(unique2)
# unique3 = s3 - s1 - s2
# print(unique3)
# # task 3
c1 = (3, 8, 5, 18, 43, 2, 8)
c2 = (3, 1, 5, 3, 4, 5, 6, 7, 8, 9)
c3 = (3, 3, 5, 69, 67, 34, 41)
limit = min(len(c1), len(c2), len(c3))
print("Елементи на однакових позиціях:")
for i in range(limit):
    if c1[i] == c2[i] == c3[i]:
        print(f"Індекс {i}: значення {c1[i]}")
