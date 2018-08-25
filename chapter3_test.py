# coding=utf-8
# 【列表】操作
test_list = [1, 4]
motorcycles = []  # 定义空的列表
print('初始的列表是这样的：')
print(motorcycles)
# 各种类型的值可以混在一起,而且列表也可以存储列表，见test_list
motorcycles = ['honda', 'yamaha', 'suzuki', '俄罗斯', 'ducati', 'toyota', 34, 'BMW', 22, 'chance', '中国', test_list]
# 访问列表的方式
print(isinstance(motorcycles[-1], str))  # 打印列表最后一个元素
print(motorcycles[-2])  # 打印列表倒数第二个元素
print('列表第一个元素是：' + motorcycles[0].title())  # 访问列表第一个元素，取出来的值，没有双引号或单引号
# 增加
motorcycles.insert(1, 23)  # 在列表的指定位置，增加一个元素
motorcycles.append(10)  # 在列表末尾增加一个元素
print(motorcycles)
# 删除
del motorcycles[1]  # 删除指定位置的元素
motorcycles.remove(34)  # 根据值，删除指定元素
motorcycles.pop()  # 删除列表最后一个元素
deleted_element = motorcycles.pop(3)
print(deleted_element)  # 推出被删掉的元素
print(motorcycles)
# 修改
motorcycles[0] = 0  # 修改列表指定元素的值
print(motorcycles)
# 排序
print("-----------------永久性排序----------------")
new_motorcycles = ['honda', 'yamaha', 'Suzuki', 'ducati']
print(new_motorcycles)
new_motorcycles.sort()  # 【永久性】顺序排序，只适用于列表元素的数据类型一致的情况，大小写元素同时存在也会有问题的！
print(new_motorcycles)
new_motorcycles.sort(reverse=True)  # 【永久性】倒序排序，只适用于列表元素的数据类型一致的情况，大小写元素同时存在也会有问题的！
print(new_motorcycles)
new_motorcycles.reverse()  # 【永久性】纯粹倒着打印列表
print(new_motorcycles)
print('new_motorcycles列表的长度是：' + str(len(new_motorcycles)))  # 打印列表的长度
print('-----------------临时性排序----------------')
print(sorted(new_motorcycles))  # 【临时性】顺序打印
print(sorted(new_motorcycles, reverse=True))  # 【临时性】倒序打印
print(new_motorcycles)
