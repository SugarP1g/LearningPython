#!/usr/bin/env python
# encoding: utf-8

"""875. 爱吃香蕉的珂珂

珂珂喜欢吃香蕉。这里有 N 堆香蕉，第 i 堆中有 piles[i] 根香蕉。警卫已经离开了，将在 H 小时后回来。

珂珂可以决定她吃香蕉的速度 K （单位：根/小时）。每个小时，她将会选择一堆香蕉，从中吃掉 K 根。如果这堆香蕉少于 K 根，她将吃掉这堆的所有香蕉，然后这一小时内不会再吃更多的香蕉。  

珂珂喜欢慢慢吃，但仍然想在警卫回来前吃掉所有的香蕉。

返回她可以在 H 小时内吃掉所有香蕉的最小速度 K（K 为整数）。

示例 1：

输入: piles = [3,6,7,11], H = 8
输出: 4
示例 2：

输入: piles = [30,11,23,4,20], H = 5
输出: 30
示例 3：

输入: piles = [30,11,23,4,20], H = 6
输出: 23

提示：

1 <= piles.length <= 10^4
piles.length <= H <= 10^9
1 <= piles[i] <= 10^9

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/koko-eating-bananas
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:

    def each_pile_eat_time(self, banana_number, eat_speed):
        return banana_number // eat_speed + (1 if banana_number % eat_speed else 0)

    def can_finish(self, piles, eat_speed, total_hour):
        total_eat_time = 0
        for pile in piles:
            total_eat_time += self.each_pile_eat_time(pile, eat_speed)

        return total_eat_time <= total_hour

    def split_search(self, start: int, end: int, piles: List[int], total_hour: int) -> int:
        if end <= start:
            return start

        middle_speed = start + (end - start) // 2

        if self.can_finish(piles, middle_speed, total_hour):
            end = middle_speed
        else:
            start = middle_speed + 1

        return self.split_search(start, end, piles, total_hour)

    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        max_number = max(piles)
        min_number = 1

        return self.split_search(min_number, max_number + 1, piles, H)


if __name__ == "__main__":
    piles = [3, 6, 7, 11]
    H = 8
    solution = Solution()
    print(solution.minEatingSpeed(piles, H))

