# def nb_year(p0, percent, aug, p):
# def nb_year(p0, percent, aug, p):
#     pop = p0
#     res = 0
#     while pop < p:
#         pop = pop * (percent+100)/100 + aug
#         res += 1
#
#     return res
#
#
# print(nb_year(1500, 5, 100, 5000))
# # 15/


# persistence(n):
# from six.moves import reduce
#
# def persistence(n):
#     res = 0
#     data = n
#     arr = []
#     while data > 9:
#         for i in str(data):
#             arr.append(int(i))
#         data = reduce(lambda x, y: x*y, arr)
#         arr = []
#
#         res +=1
#
#     return res
#
#
# print(persistence(17))
