def summary_ranges(nums):
    # Store the final answer
    result = []

    # Pointer to traverse the array
    i = 0

    # Traverse until all elements are processed
    while i < len(nums):

        # First number of the current range
        start = nums[i]

        # Continue while the next number is consecutive
        while i + 1 < len(nums) and nums[i + 1] == nums[i] + 1:
            i += 1

        # If start and end are the same, it's a single number
        if start == nums[i]:
            result.append(str(start))
        else:
            # Otherwise, store the complete range
            result.append(str(start) + "->" + str(nums[i]))

        # Move to the next unprocessed number
        i += 1

    return result


print(summary_ranges([0, 1, 2, 4, 5, 7]))