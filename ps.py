# # task 1
# mista = "Chernihiv","Uman","Kyiv","Boryspil","Dnipro","Kyiv"
# unq = tuple(set(filter(lambda x: mista.count(x) > 1, mista)))
# print(unq)
# # task 2
# import random
#
# nums1 = tuple(random.randrange(1,101) for x in range(10))
# nums2 = tuple(random.randrange(1,101) for i in range(10))
#
# unq1 = tuple(set(filter(lambda x: x not in nums2, nums1)))
# unq2 = tuple(set(filter(lambda x: x not in nums1, nums2)))
# sam1 = tuple(set(filter(lambda x: x in nums2, nums1)))
#
# print(f"Ye v pershomu ale nema v drugomu: {unq1}")
#
# print(f"Ye v drugomu ale nema v pershomu: {unq2}")
#
# print(f"I tam i tam: {sam1}")
# # task 3
# cort = "Mavpa",1,59,43,6,8,2,9,3,6,17
# cort2 = "Mavpa","Mlynci","Hvozdi","Terorysty","d","f","d","d",3
# rs = list(set(a for a,b in zip(cort,cort2) if a == b))
# print(rs)
