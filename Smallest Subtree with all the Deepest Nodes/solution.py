# Intuition
# The deepest nodes are the ones with the maximum depth in the tree.
# The smallest subtree containing all deepest nodes is their lowest common ancestor.
# So the problem reduces to finding the node where the deepest nodes from the left and right subtrees meet.

# Approach
# 1. Use a depth-first search that returns two things for each node:
#    - The maximum depth in its subtree.
#    - The node that represents the smallest subtree containing all deepest nodes.
# 2. For each node:
#    - Recursively compute results for left and right children.
#    - If left depth is greater, return the left result.
#    - If right depth is greater, return the right result.
#    - If depths are equal, the current node is the answer.
# 3. The final returned node is the root of the smallest subtree containing all deepest nodes.

# Complexity
# - Time complexity: O(n)
#   Each node is visited exactly once.

# - Space complexity: O(h)
#   Due to recursion stack, where h is the height of the tree.

# Code
class Solution:
    def subtreeWithAllDeepest(self, root):
        def dfs(node):
            if not node:
                return 0, None

            left_depth, left_node = dfs(node.left)
            right_depth, right_node = dfs(node.right)

            if left_depth > right_depth:
                return left_depth + 1, left_node
            if right_depth > left_depth:
                return right_depth + 1, right_node

            return left_depth + 1, node

        return dfs(root)[1]