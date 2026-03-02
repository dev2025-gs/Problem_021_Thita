def findMaxAverage(nums, k):
    """
    Finds the maximum average of any contiguous subarray of length k in the list nums.
    :type nums: List[int]
    :type k: int
    :rtype: float
    """
    n = len(nums)  # Get the length of the input list

    # Compute the sum of the first window of size k
    window_sum = sum(nums[:k])

    # Initialize max_sum with the sum of the first window
    max_sum = window_sum

    # Slide the window through the array
    # For each step, subtract the element going out and add the new element coming in
    for i in range(n - k):
        window_sum = window_sum - nums[i] + nums[i + k]  # Update the window sum
        max_sum = max(window_sum, max_sum)  # Update max_sum if current window_sum is greater

    # Return the maximum average found
    return max_sum / k

# Example usage:
x = [1, 12, -5, -6, 50, 3]  # Input list
y = 4  # Window size
ans = findMaxAverage(x, y)  # Call the function
print(ans)  # Print the result