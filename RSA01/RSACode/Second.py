# -*- coding: utf-8 -*-

'''
超大整数超大次幂然后对超大的整数取模
蒙哥马利算法 幂模转换为乘模
(base ^ exponent) mod n
'''
import time

# 将幂转换为进制数据
# c = exp_mode(m, e, n)
def exp_mode(base, exponent, n):
    # 取下标2到最后（去除二进制），  然后逆置
    bin_array = bin(exponent)[2:][::-1]
    # print("bin_array:"+bin_array)
    r = len(bin_array)
    base_array = []

    pre_base = base
    base_array.append(pre_base)
    #     下划线表示 临时变量， 仅用一次，后面无需再用到
    for _ in range(r - 1):
        next_base = (pre_base * pre_base) % n
        base_array.append(next_base)
        pre_base = next_base
    # base_array 存放数据a  bin_array存放b数据的二进制
    a_w_b = __multi(base_array, bin_array, n)
    # 每次计算都进行取模运算
    return a_w_b % n


def __multi(array, bin_array, n):
    result = 1
    for index in range(len(array)):
        a = array[index]
        # 如果二进制即指数为0时乘积为1，直接跳过
        if not int(bin_array[index]):
            continue
        result *= a
        result = result % n  # 加快连乘的速度
    return result
