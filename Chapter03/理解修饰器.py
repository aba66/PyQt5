# def f1(arg):
#     print("这是f1")
#     f2()
#
# def f2():
#     print("这是f2")
#
# f1(f2)


# def f1(arg):
#     print('这是f1')
#     def f2():
#         print('这是f2')
#         return arg()
#     return f2
#
# def f3():
#     print("这是f3")
#
# f3 = f1(f3)  # f1就叫闭包函数
# f3()


# 等价于上一段
# def f1(arg):
#     print('这是f1')
#
#     def f2():
#         print('这是f2')
#         return arg()
#     return f2
#
#
# @f1
# def f3():
#     print("这是f3")
#
#
# f3()  # 说明修饰器本质就是闭包


# 因为第一层闭包函数需要参数，所以就把传递func的工作交给第二层
# def log_wrapper(s):
#     def pre_improve_func(func):
#         def improve_func(str):
#             func(str)
#             print(s)
#             return
#         return improve_func
#     return pre_improve_func
#
#
# @log_wrapper(s='a try')
# def func(arg):
#     print(arg)
#     pass
#
# func('66')

# 和上一个是等价的
# def log_wrapper(s):
#     def pre_improve_func(func):
#         def improve_func(str):
#             func(str)
#             print(s)
#             return
#         return improve_func
#     return pre_improve_func
#
#
# # @log_wrapper(s='a try')
# def func(arg):
#     print(arg)
#     pass
#
# temp = func
# func = log_wrapper(s='a try')
# func = func(temp)
# func('66')