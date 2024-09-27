# """
# 1.类属性，在def之外（可动态添加属性）
# 2.实例属性，在def之内（只作用于当前例）
# """
#
#
# class Geese:
#     """大雁类型"""
#     beak1 = '01'
#     wing2 = '10'
#     claw3 = '11'
#     number = 0
#
#     def __init__(self):
#         Geese.number += 1
#         print('\nNO.', Geese.number)
#         print("大雁")
#         print(Geese.beak1)
#         print(Geese.wing2)
#         print(Geese.claw3)
#
#     def fly(self, state):
#         print(state)
#
#
# list1 = []
# for i in range(3):
#     list1.append(Geese())
# print('list1')
#
# Geese.cc = '^_^'
# print('test', list1[1].cc)


# 访问限制

class Swan:
    """天鹅"""
    _neck_swan = 'long'

    def __init__(self):
        print("__init__():", Swan._neck_swan)


swan = Swan()
print('direct:', swan._neck_swan)


class wan2:
    """天鹅"""
    __neck_wan2 = 'long'

    def __init__(self):
        print("__init__():", wan2.__neck_wan2)


swan2 = wan2()
print('add:', wan2._wan2__neck_wan2)     # 这样可以访问：'实例名._类名__xxx'
print('direct:', wan2.__neck_wan2)        # 这个不行
