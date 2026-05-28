# Plus One Problem
# Problem: Given a list of digits representing a non-negative integer,
# add one to the integer and return the resulting list of digits.

from typing import List

# ------------------------------------------------------------
# Attempt 1: 
# ------------------------------------------------------------
class SolutionAttempt1:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1
        return digits

# Works for [1,2,3] → [1,2,4]
# Fails for [9,9] → [9,10] (invalid digit)
# Issue: Doesn't handle carry when last digit is 9.


# ------------------------------------------------------------
# Attempt 2: 
# ------------------------------------------------------------
class SolutionAttempt2:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1, -1, -1):
            if digits[-1] == 9:   
                digits[-1] = 0
                digits.insert(0, 1)
            else:
                digits[-1] += 1
        return digits

# Problem: Always modifies digits[-1], ignoring i.
# Example: [1,2,3] → [1,2,6] (wrong).
# Issue: Loop is useless because it doesn’t use the loop variable.


# ------------------------------------------------------------
# Attempt 3: 
# ------------------------------------------------------------
class SolutionAttempt3:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + digits

# Works for [1,2,3] → [1,2,4]
# Works for [9,9] → [1,0,0]
# Works for [9,9,9] → [1,0,0,0]
# Fix: Uses i properly, handles carry, prepends 1 if all digits are 9.


# ------------------------------------------------------------
# Final Solution: 
# ------------------------------------------------------------
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + digits


# ------------------------------------------------------------
# Dry Run Example
# ------------------------------------------------------------
# Input: [9,9]
# i=1 → digit=9 → set to 0, carry continues
# i=0 → digit=9 → set to 0, carry continues
# Loop ends → prepend [1] → [1,0,0] 

# ------------------------------------------------------------
# Test Cases
# ------------------------------------------------------------
sol = Solution()
print(sol.plusOne([1,2,3]))   # [1,2,4]
print(sol.plusOne([9,9]))     # [1,0,0]
print(sol.plusOne([9,9,9]))   # [1,0,0,0]
print(sol.plusOne([4,5,6]))   # [4,5,7]
