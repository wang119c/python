# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf8')


# 深度优先算法
def depth_tree(tree_node):
    if tree_node is not None:
        print tree_node._data
    if tree_node._left is not None:
        return depth_tree(tree_node._left)
    if tree_node._right is not None:
        return depth_tree(tree_node._right)
