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

    # Test Case 1: Example from problem
    vals1 = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
    root1 = build_tree(vals1)
    result1 = sol.subtreeWithAllDeepest(root1)
    print("Test 1 - Expected: 2, Got:", result1.val if result1 else None)
    assert result1.val == 2, f"Test 1 failed: expected 2, got {result1.val}"

    # Test Case 2: Single node
    vals2 = [1]
    root2 = build_tree(vals2)
    result2 = sol.subtreeWithAllDeepest(root2)
    print("Test 2 - Expected: 1, Got:", result2.val if result2 else None)
    assert result2.val == 1, f"Test 2 failed: expected 1, got {result2.val}"

    # Test Case 3: Two levels
    vals3 = [1, 2, 3]
    root3 = build_tree(vals3)
    result3 = sol.subtreeWithAllDeepest(root3)
    print("Test 3 - Expected: 1, Got:", result3.val if result3 else None)
    assert result3.val == 1, f"Test 3 failed: expected 1, got {result3.val}"

    print("All tests passed!")