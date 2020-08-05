#!/usr/bin/env python
# encoding: utf-8

"""204. 计数质数

统计所有小于非负整数 n 的质数的数量。

示例:

输入: 10
输出: 4
解释: 小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
"""


class Solution:
    def countPrimes(self, n: int) -> int:
        # 前 2 个数不是素数
        if n < 3:
            return 0
        # isprime 数组
        isprime = [1] * n

        for i in range(2, int(n ** 0.5) + 1):
            if isprime[i]:
                # 从 i*i（包括自己） 到 n（不包括n），每步增加 i 的所有数的个数
                tmp = ((n - 1 - i * i) // i + 1)
                # 这种方式赋值比用 for 循环更高效
                isprime[i * i: n: i] = [0] * tmp

        # 前 2 个数不是素数，去掉
        count = sum(isprime[2:])
        return count
