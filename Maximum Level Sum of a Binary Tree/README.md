# 1161. Maximum Level Sum of a Binary Tree

# Intuition
We can traverse the binary tree level by level (BFS). At each level, sum the node values and track the level with the maximum sum seen so far.

# Approach
- Use a queue (`deque`) initialized with the root.
- For each level, iterate exactly `len(queue)` times to process nodes in that level, accumulating their values.
- Enqueue left and right children for the next level.
- If the current level's sum exceeds the recorded maximum, update `max_sum` and `max_level`.
- Return the 1-indexed `max_level` after traversal.

# Complexity
- Time complexity: $$O(n)$$ where $n$ is the number of nodes, since each node is visited once.
- Space complexity: $$O(w)$$ where $w$ is the maximum width of the tree (worst-case $$O(n)$$ for a complete tree), due to the queue.

# Code
```python
from collections import deque

class Solution(object):
    def maxLevelSum(self, root):
        queue = deque([root])
        max_sum = float('-inf')
        max_level = 1
        level = 1

        while queue:
            level_sum = 0
            for _ in range(len(queue)):
                node = queue.popleft()
                level_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if level_sum > max_sum:
                max_sum = level_sum
                max_level = level
            level += 1

        return max_level
```