import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from twosum import solution

# Test case 1: Basic example
nums = [2, 7, 11, 15]
target = 9
expected_output = [0, 1]
assert solution.twosum(nums, target) == expected_output

# Test case 2: No solution
nums = [2, 7, 11, 15]
target = 10
expected_output = None
assert solution.twosum(nums, target) == expected_output

# Test case 3: Multiple solutions
nums = [3, 2, 4]
target = 6
expected_output = [1, 2]
assert solution.twosum(nums, target) == expected_output

# Test case 4: Empty list
nums = []
target = 9
expected_output = None
assert solution.twosum(nums, target) == expected_output
