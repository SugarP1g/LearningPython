#!/usr/bin/env python
# encoding: utf-8

"""815. 公交路线

我们有一系列公交路线。每一条路线 routes[i] 上都有一辆公交车在上面循环行驶。
例如，有一条路线 routes[0] = [1, 5, 7]，表示第一辆 (下标为0) 公交车会一直按照 1->5->7->1->5->7->1->... 的车站路线行驶。

假设我们从 S 车站开始（初始时不在公交车上），要去往 T 站。 期间仅可乘坐公交车，求出最少乘坐的公交车数量。返回 -1 表示不可能到达终点车站。

示例：
    输入：
    routes = [[1, 2, 7], [3, 6, 7]]
    S = 1
    T = 6
    输出：2
    解释：
    最优策略是先乘坐第一辆公交车到达车站 7, 然后换乘第二辆公交车到车站 6。

提示：
    1 <= routes.length <= 500.
    1 <= routes[i].length <= 10^5.
    0 <= routes[i][j] < 10 ^ 6.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/bus-routes
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

import collections

from typing import List


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        if S == T:
            return 0
        routes = list(map(set, routes))
        graph = collections.defaultdict(set)
        for i, r1 in enumerate(routes):
            for j in range(i + 1, len(routes)):
                r2 = routes[j]
                if any(r in r2 for r in r1):
                    graph[i].add(j)
                    graph[j].add(i)

        seen, targets = set(), set()
        for node, route in enumerate(routes):
            if S in route:
                seen.add(node)
            if T in route:
                targets.add(node)

        queue = [(node, 1) for node in seen]
        for node, depth in queue:
            if node in targets:
                return depth
            for nei in graph[node]:
                if nei not in seen:
                    seen.add(nei)
                    queue.append((nei, depth + 1))
        return -1


if __name__ == "__main__":
    routes = [[1, 2, 7], [3, 6, 7]]
    S = 1
    T = 6
    solution = Solution()
    print(solution.numBusesToDestination(routes, S, T))
