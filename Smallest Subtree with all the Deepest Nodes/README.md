# Smallest Subtree with all the Deepest Nodes

Given the root of a binary tree, the deepest leaves are the nodes at the deepest level. The smallest subtree that contains all the deepest leaves is called the smallest subtree with all the deepest nodes.

Return the root of that subtree.

## Example

Input: root = [3,5,1,6,2,0,8,null,null,7,4]
Output: [2,7,4]

Explanation: The deepest leaves are [7,4,0,8]. The smallest subtree containing all of them is the subtree rooted at 2.

## Constraints

- The number of nodes in the tree will be in the range [1, 500].
- 0 <= Node.val <= 50
- All Node.val are unique.