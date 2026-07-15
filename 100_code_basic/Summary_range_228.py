def summary_range(nums):
    result = []
    i = 0

    while i < len(nums):

        start = nums[i]

        while i + 1 < len(nums) and nums[i + 1] == nums[i] + 1:
            i += 1

        if start == nums[i]:
            result.append(str(start))
        else:
            result.append(f"{start}->{nums[i]}")

        i += 1

    return result


print(summary_range([0,1,2,4,5,7]))