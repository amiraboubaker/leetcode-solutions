## Intuition
The goal is to find the largest square subgrid where all row sums, column sums, and both diagonal sums are equal. Checking all sums directly for every possible square would be inefficient, so prefix sums are used to compute these values quickly and allow fast validation of each candidate square.

## Approach
First, compute prefix sums for rows, columns, and both diagonals of the grid. Then iterate over all possible square sizes starting from the largest. For each k × k subgrid, use the prefix sums to compute a target sum and verify that all rows, columns, and diagonals match this sum. Return the size of the first valid magic square found. If none exists, return 1 since a 1 × 1 square is always magic.

## Complexity
- Time complexity:  
  O(min(m, n)³)

- Space complexity:  
  O(m × n)