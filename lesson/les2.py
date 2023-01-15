# Если выписать все натуральные числа меньше 10, кратные 3 или 5, то получим 3, 5, 6 и 9. Сумма этих чисел равна 23.
# Найдите сумму всех чисел меньше 1000, кратных 3 или 5.
# a = 0
# for i in range(1000):
#     if i < 10 and (i%3==0 or i%5==0):
#         a = a + i
# # print(a)
# b = [i for i in range(1,1000) if i <10 and (i%3==0 or i%5==0)]
# print(sum(b))
# a = 10
# for i in range(a):
#     print(i)
# def my_funk(start, stop, step):
#     if start >= stop:
#         return start
#     else:
#         print(start)
#         my_funk(start + step, stop, step) # рекурсия
# my_funk(0,10,1)
# a = 5
# def loc_var(b):
#     global a
#     a = 'hello word'
#     # b = 0
#     # a = b
#     print(a, 'kkk')
# print(a)
# loc_var(6)
# SP = None
# def my_funk(spisok: list) -> list:
#     if spisok is None:
#         print('yes')
# my_funk(SP)
# def a():
#     b()
# def b():
#     c()
# def c():
#     print('run c')
# a()
# def fact(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * fact(n - 1)
# print(fact(5))
# 3! = 1*2*3
# Sp = [2, 3]
# print(*Sp, 'lll')
# def my_funk(spisok, par):
#     return spisok, par
# print(my_funk(*Sp)) оператор распаковки

# dict = {'a': 1, 'b': 2}
# def unpak_dick(a,b):
#     return a, b
# print(unpak_dick(**dict))