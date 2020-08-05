#!/usr/bin/env python
# encoding: utf-8

"""面试题 04.03. 特定深度节点链表


给定一棵二叉树，设计一个算法，创建含有某一深度上所有节点的链表（比如，若一棵树的深度为 D，则会创建出 D 个链表）。返回一个包含所有深度的链表的数组。

示例：

输入：[1,2,3,4,5,null,7,8]

        1
       /  \
      2    3
     / \    \
    4   5    7
   /
  8

输出：[[1],[2,3],[4,5,7],[8]]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/list-of-depth-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return str(self.val)


def list_node_append(node_list: ListNode, new_node: ListNode) -> None:
    tail_node = node_list
    while tail_node.next is not None:
        tail_node = tail_node.next

    tail_node.next = new_node


class Solution:

    def _traverse(self, current_node: TreeNode, index: int, result_node_list: List[ListNode]) -> None:

        if current_node is None:
            return

        current_level_list_node = ListNode(current_node.val)
        try:
            node_link_list = result_node_list[index]
        except IndexError:
            result_node_list.append(current_level_list_node)
        else:
            list_node_append(node_link_list, current_level_list_node)

        self._traverse(current_node.left, index + 1, result_node_list)
        self._traverse(current_node.right, index + 1, result_node_list)

    def listOfDepth(self, tree: TreeNode) -> List[ListNode]:
        result_node_list = []
        self._traverse(tree, 0, result_node_list)
        return result_node_list


def fake_input() -> TreeNode:
    root_node = TreeNode(1)
    root_node.left = TreeNode(2)
    root_node.right = TreeNode(3)
    root_node.left.left = TreeNode(4)
    root_node.left.right = TreeNode(5)
    root_node.right.right = TreeNode(7)
    root_node.left.left.left = TreeNode(8)
    return root_node


if __name__ == "__main__":
    input_data = fake_input()
    solution = Solution()
    result = solution.listOfDepth(input_data)
    for sub_node_list in result:
        while sub_node_list is not None:
            print(sub_node_list.val, end=' ')
            sub_node_list = sub_node_list.next
        print()
