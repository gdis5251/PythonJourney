# 元祖不能被修改
# def get_point():
#     return 10, 20
# x, y = get_point()
# print(x, y)

# 加个逗号就会表示为元祖
# 不加就会被认为是整数
# a = (10 + 20) * 3
# b = (10 + 20, ) * 3
# print(type(a))
# print(a)
# print(type(b))
# print(b)

# 元祖的两个重要应用场景
# 1. 函数传参的时候使用元祖可以避免把函数外面的内容修改掉
# a = [10, 20, 30]
# a = (10, 20, 30)
# def func(input_list):
#     input_list[0] = 100
# func(a)
# print(a)
# 2. 元祖是可哈希的，元祖就可以作为字典的 key 而列表不行 
# a = (1, 2, 3)
# # a = [1, 2, 3] // 会报错
# b = {
#     a: 100
# }
# print(b)