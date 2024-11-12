# python overwrites previous implementation ALWAYS
# class test:
#     def wow(self):
#         print('wow')
#     def wow(self, a):
#         print('owo')


# test().wow(1)

# when multiple inheritance, this case is useful since we can access wow methods of both testA and testO
# instead of relying on super() which only calls the method of the first class inherited

# class testO:
#     def wow(self):
#         print('testO')

# class testA:
#     def wow(self):
#         print('testA')

# class testB(testA, testO):
#     def wow(self):
#         testA.wow(self)
#         testO.wow(self)
#         print('testB')

#     def wowy(self):
#         testA.wow(self)

# testB().wow()

# normally, an object can't use static methods since it's not associated to it, but by adding static method,
# you can use the method

# class testS:
#     __thing = 0

#     @staticmethod
#     def set_thing(x):
#         testS.__thing = x

#     def get_thing():
#         return testS.__thing

# a = testS()
# a.set_thing(2)
# print(testS.get_thing())


# if self used for value then value only changes for current instance
# and if you really want to use self but still want to change the value
# you can use classmethod

# class test:
#     value = 1
#
#     @classmethod
#     def set_val(self, x):
#         self.value = x

# a = test()
# a.set_val(2)
# print(test.value)