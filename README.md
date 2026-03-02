# Problem_021_Thita
# Maximum Average Subarray I

## 🧩 Problem Description

You are given an integer array `nums` consisting of `n` elements, and an integer `k`.

Your task is to find a **contiguous subarray** of length `k` that has the **maximum average value**, and return this value.

Any answer with a calculation error less than `10^-5` will be accepted. 
https://thita.ai/problems/maximum-average-subarray-i

---

## 📌 Examples

### Example 1

**Input:**
nums = [1,12,-5,-6,50,3], k = 4


**Output:**
12.75000


**Explanation:**

The subarray `[12, -5, -6, 50]` has the maximum average:

(12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75


---

### Example 2

**Input:**

nums = [5], k = 1


**Output:**

5.00000


---

## 📋 Constraints

- `n == nums.length`
- `1 <= k <= n <= 10^5`
- `-10^4 <= nums[i] <= 10^4`

---

## 💡 Approach

### Sliding Window Technique

Since the subarray must be **contiguous** and of fixed length `k`, we can use a **sliding window** approach:

1. Compute the sum of the first `k` elements.
2. Store it as the initial maximum sum.
3. Slide the window one element at a time:
   - Subtract the element leaving the window.
   - Add the new element entering the window.
4. Update the maximum sum whenever a larger sum is found.
5. Return `max_sum / k`.

This approach avoids recalculating sums repeatedly and ensures efficiency.
Source: https://www.geeksforgeeks.org/dsa/window-sliding-technique/

---

## 🧠 Key Insight

Instead of recomputing the sum of each `k`-length subarray from scratch (which would take `O(nk)`), the sliding window allows us to update the sum in constant time for each step.

This makes the solution optimal and scalable up to `10^5` elements.

---

## ✅ Summary

- Use a fixed-size sliding window.
- Track the maximum sum encountered.
- Return the maximum average (`max_sum / k`).
- Efficient and clean `O(n)` solution.

---
