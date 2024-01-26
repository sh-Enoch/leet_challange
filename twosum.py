class solution:
    """
    Class to find the indices of two numbers in a list that add up to a target value.
    """

    def twosum(self, nums, target):
        """
        Finds the indices of two numbers in the given list that add up to the target value.

        Args:
            nums (List[int]): The list of numbers.
            target (int): The target value.

        Returns:
            List[int]: The indices of the two numbers that add up to the target value.
        """
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
