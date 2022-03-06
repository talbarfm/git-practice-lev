def sum67(nums):
    """
    Gets the sum of the numbers in the array, except ignore sections of numbers starting with a 6
    and extending to the next 7
     param: nums(list): A list of numbers.
    return: Number of sum
    """
    new_list = []
    while 6 in nums:
        index_six = nums.index(6)
        new_list.extend(nums[:index_six])
        nums = nums[index_six:]
        nums = nums[nums.index(7) + 1:]
    new_list.extend(nums)
    return sum(new_list)


def main():
    print(sum67([1, 2, 3, 4, 5, 6, 7, 2, 3, 6, 2, 3, 7, 0, 1]))
    print(sum67([]))


if __name__ == "__main__":
    main()
