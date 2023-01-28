# list1 = {*range(1,10,2)}

# print(list1)
#dict = {x: x**3 for x in range (2,11,2)}
#print(dict)
# nums ={ 'x':'10' , 'y':'20' , 'z':'30', 'p':'40', 'q':'50', 'r':'60'}
# for key, v in nums.items():
    # try:
#         v = int(v)
#     except:
#         pass
#     nums[key] = v
# print(nums)

# def pretty_print (**kwargs):
#    for a in kwargs:
#     print(f'{a}:{kwargs[a]}')
# pretty_print(title="The Matrix", director="Wachowski", year=1999)
# def is_anagram (str1, str2):
#     return set(str1) == set(str2)
#
# def make_matrix(size, value=0):
#     if type(size) == int:
#         rows = size
#         cols = size
#     else:
#         rows = size[1]
#         cols = size[0]
#     return [
#         [
#             value for c in range(cols)
#         ]for r in range(rows)
#     ]
# result = make_matrix(3)
# result2 = make_matrix((4,2), 1)
# print(result)
# print(result2)
# def decorator(func):
#     def inner(a, b):
#         return func(a*2, b*2)
#     return inner
# @decorator
# def sum(a, b):
#     return a + b
#
# # print((1, 2))
# # sum = decorator(sum)
# print(sum(1,2))
# list = [*range(2,101,2)]
# print(list)
# for i in range(100):
#     if i % 2 == 0:
#         print (i)
