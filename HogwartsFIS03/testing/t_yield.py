
# yield 生成器
def provider():
    # 循环读取数据列表
    for i in range(10):
        print("开始操作")
        # 相当于return i，记录上一次执行位置
        yield i
        print("结束操作")

p = provider()
# 打印出来的对象类型就是生成器 gennerator
# print(p)

# print(next(p))
# print(next(p))
# print(next(p))
# print(next(p))
# print(next(p))

for i in p:
    print(i)
