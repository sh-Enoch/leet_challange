def search_target(nums, target):
    """Go through nums and find the indices of numbers that add up to target."""
    new_list = []

    for num in range(len(nums)):
        for j in range(num+1, len(nums)):
            if nums[num] + nums[j] == target:
                new_list.append(num)
                new_list.append(j)
    return new_list
