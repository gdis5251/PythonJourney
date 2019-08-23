# import copy

# a = [1, 2, 3, 4]
# 在最后插入元素
# a.append(5)
# print(a)

# help(list)

# a.insert(1, 100)
# print(a)

# 列表拼接
# b = [5, 6, 7]
# print(len(a+b), a + b)
# # a.append(b)
# a.extend(b)
# print(len(a), a)

# 删除元素
# del(a[3])
# a.remove(3)
# 填-1表示删除最后一个元素
# a.pop(1)
# print(a)

# 模拟实现栈
# a.append(10)
# print(a)
# a.pop()
# print(a)

# # 模拟实现队列
# a.append(100)
# print(a)
# del(a[0])
# # a.pop(0)
# print(a)


# 列表翻转
# a = [10, 20, 30, 40]
# print(a[::-1])
# a.reverse()
# print(a)


# 深拷贝 浅拷贝
# a = [10, 20, 30, 40]
# b = a
# a[0] = 100
# # 说明是浅拷贝
# print(b)

# 实现深拷贝
# 深拷贝只能针对可变对象使用
# 深拷贝的目的就是说改了一个另一个不改变
# 而如果对象不可改变，就失去了需求
# b = copy.deepcopy(a)
# a[0] = 100
# print(b)


