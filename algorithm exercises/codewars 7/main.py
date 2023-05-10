# def digital_root(n: int):
#     arr = []
#     result = n
#     while result > 9:
#         for i in str(result):
#             print(i)
#             arr.append(int(i))
#
#         result = sum(arr)
#         arr = []
#     return result

def digital_root(n: int):
    return n % 9 or n and 9


132189
print(digital_root(942))
# digital_root(132189)
# digital_root(493193)
