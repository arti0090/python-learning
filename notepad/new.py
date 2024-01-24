# class Ex(Exception):
#     def __init__(self, msg):
#         Exception.__init__(self, msg + msg)
#         self.args = (msg,)

# try:
#     raise Ex('ex')
# except Ex as e:
#     print(e)
# except Exception as e:
#     print(e)

# ==========================

# class A:
#     pass
# class B(A):
#     pass
# class C(A):
#     pass

# print(issubclass(C,A))

# ==========================

# try:
#     raise Exception(1,2,3)
# except Exception as e:
#     print(e.args)

# ==========================

# class A:
#     def a(self):
#         print('a')
# class B:
#     def a(self):
#         print('b')
# class C(B,A):
#     def c(self):
#         self.a()

# C().c()

# ==========================

# def I():
#     s = 'abcdef'
#     for c in s[::2]:
#         yield c
# for x in I():
#     print(x, end='')

# ==========================

# def o(p):
#     def q():
#         return '*' * p
#     return q

# r = o(1)
# s = o(2)
# print(r() + s())

# ==========================

# def I(n):
#     s = '+'
#     for i in range(n):
#         s += s
#         yield s
# for x in I(2):
#     print(x, end='')

# ==========================

# class I:
#     def __init__(self):
#         self.s = 'abc'
#         self.i = 0
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.i == len(self.s):
#             raise StopIteration
#         v = self.s[self.i]
#         self.i += 1
#         return v
# for x in I():
#     print(x, end='')

# ==========================

# class A:
#     X = 0
#     def __init__(self, v = 0):
#         self.Y = v
#         A.X += v

# a = A()
# b = A(1)
# c = A(2)
# print(c.X)

# ==========================

# class A:
#     def __init__(self):
#         pass

# a = A(1)
# print(hasattr(a, 'A'))

# ==========================

# class A:
#     def __init__(self):
#         self.a = 1

# class B:
#     def __init__(self):
#         A.__init__(self)
#         self.b = 2

# print(B().b)

# ==========================
# ==========================

# class A:
#     A = 1
#     def __init__(self):
#         self.a = 0

# print(hasattr(A, 'A'))

# ==========================

# try:
#     raise Exception
# except:
#     print('x')
# except Exception:
#     print('d')

# ==========================

# try:
#     raise Exception
# except BaseException:
#     print('a')
# except Exception:
#     print('d')
# except:
#     print('x')

# ==========================

# ls = [[c for c in range(r)] for r in range(3)]
# for x in ls:
#     if len(x) < 2:
#         print()

# ==========================

# t = (1, )
# t = t[0] + t[0]
# print(t)

# ==========================

# i = 4

# while i > 0:
#     i -= 2
#     print("*")
#     if i == 2:
#         break
# else:
#     print("*")

# ==========================

# d = { 1:0, 2:1, 3:2, 0:1 }
# x = 0

# for y in range(len(d)):
#     x = d[x]

# print(x)

# ==========================

# print(len([i for i in range(0, -2)]))

# ==========================

# def fun(x):
#     return 1 if x % 2 != 0 else 2

# print(fun(fun(1)))

# ==========================

# x = 16
# while x > 0:
#     print('x')
#     x //= 2

# ==========================

# t = (1,2,3,4)
# t = t[-2: -1]
# print(t[-1])

# ==========================

# def fun(d, k, v):
#     d[k] = v

# dc = {}
# print(fun(dc, '1', 'v'))

# ==========================

class A:
    def __init__(self, name):
        self.name = name
    def __str__(self) -> str:
        return 'xd'

print(A("class"))
print(len((1,)))