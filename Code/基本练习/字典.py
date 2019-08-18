# 列表解析， 用一个表达式构造列表
# 字典解析， 用一个表达式构造字典

# 字典的 key 必须是可哈希，不可变是可哈希的必要条件

# 判断这个元素是否可哈希
# print(hash((10)))
# print(hash([10]))

# a = (1, 2, 3)
# # a = [1, 2, 3] // 会报错
# b = {
#     a: 100
# }
# print(b)

a = {
    'ip': '127.0.0.1',
    'port': 80
}

# print(a['ip'])
# print(a['port'])

# for key in a:
#     print(key, a[key])

# 只能改 value 不可以改 key
# a['ip'] = '47.101.192.120'
# print(a)

# key 不存在就插入
# a['id'] = 'Gerald Kwok'
# print(a)
# # key 不存在 打印抛异常
# print(a['jeje'])

# del(a['ip'])
# print(a)

# 哈希的线程安全问题


# 比较
# 先比较长度
# 比较 key
# 比较 value

# 内置函数
print(a.keys())
print(a.values())
print(a.items())