from collections import deque
from solution import Solution

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(values):
    """
    Build a binary tree from a level-order list with None as missing nodes.
    """
    if not values:
        return None

    it = iter(values)
    root_val = next(it)
    root = TreeNode(root_val) if root_val is not None else None
    queue = deque([root])

    while queue:
        node = queue.popleft()
        try:
            left_val = next(it)
        except StopIteration:
            break
        if node is not None and left_val is not None:
            node.left = TreeNode(left_val)
        queue.append(node.left if node and node.left else None)

        try:
            right_val = next(it)
        except StopIteration:
            break
        if node is not None and right_val is not None:
            node.right = TreeNode(right_val)
        queue.append(node.right if node and node.right else None)

    return root


if __name__ == "__main__":
    sol = Solution()

    # Test Case 1
    vals1 = [1, 7, 0, 7, -8, None, None]
    root1 = build_tree(vals1)
    result1 = sol.maxLevelSum(root1)
    expected1 = 2
    print(f"Test 1: Output: {result1}, Expected: {expected1} - {'Accepted' if result1 == expected1 else 'Failed'}")

    # Test Case 2
    vals2 = [989, None, 10250, 98693, -89388, None, None, None, -32127]
    root2 = build_tree(vals2)
    result2 = sol.maxLevelSum(root2)
    expected2 = 2
    print(f"Test 2: Output: {result2}, Expected: {expected2} - {'Accepted' if result2 == expected2 else 'Failed'}")
