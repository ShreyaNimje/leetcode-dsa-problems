# Special Character Problem
# -------------------------
# Problem: Count how many lowercase letters in a string have their uppercase version
# also present, AND the lowercase must appear before the uppercase in the string.

# ------------------------------------------------------------
# Attempt 1:
# ------------------------------------------------------------
class SolutionAttempt1:
    def numberOfSpecialChars(self, word: str) -> int:
        n = len(word)
        count = 0
        for i in range(n):
            if word[i].islower():  # ✅ check lowercase
                for j in range(i+1, n):  # ✅ check later characters
                    if word[j] == word[i].upper():
                        count += 1
                        break
        return count

# Works for simple cases like "aA"
# Wrong for cases like "AbBCab" because uppercase comes first.
# nefficient: O(n^2) nested loops.


# ------------------------------------------------------------
# Attempt 2:
# ------------------------------------------------------------
class SolutionAttempt2:
    def numberOfSpecialChars(self, word: str) -> int:
        chars = set(word) 
        count = 0
        for ch in chars:
            if ch.islower() and ch.upper() in chars:
                count += 1
        return count

# Faster, avoids nested loops
# Wrong for "AbBCab" → returns 2 instead of 0
# Reason: set ignores order, so it only checks existence, not positions.


# ------------------------------------------------------------
# Attempt 3: 
# ------------------------------------------------------------
class SolutionAttempt3:
    def numberOfSpecialChars(self, word: str) -> int:
        first_lower = {}
        first_upper = {}
        
        for i, ch in enumerate(word):
            if ch.islower() and ch not in first_lower:
                first_lower[ch] = i
            elif ch.isupper() and ch not in first_upper:
                first_upper[ch] = i
        
        count = 0
        for ch, idx in first_lower.items():
            if ch.upper() in first_upper and idx < first_upper[ch.upper()]:
                count += 1
        return count

# Correctly handles order
# But fails if lowercase appears multiple times after uppercase
# Example: "aaAbcBC" → expected 3, but may miscount.


# ------------------------------------------------------------
# Final Solution: 
# ------------------------------------------------------------
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        first_upper = {}
        last_lower = {}
        
        for i, ch in enumerate(word):
            if ch.isupper() and ch not in first_upper:
                first_upper[ch] = i
            elif ch.islower():
                last_lower[ch] = i
        
        count = 0
        for ch, last_idx in last_lower.items():
            if ch.upper() in first_upper and last_idx < first_upper[ch.upper()]:
                count += 1
        return count


# ------------------------------------------------------------
# Dry Run Example
# ------------------------------------------------------------
# Input: "AbBCab"
# first_upper = {'A':0, 'B':2, 'C':3}
# last_lower  = {'b':5, 'a':4}
# Check 'b': last_idx=5, first_upper['B']=2 → 5 < 2? 
# Check 'a': last_idx=4, first_upper['A']=0 → 4 < 0? 
# Result = 0 

# ------------------------------------------------------------
# Test Cases
# ------------------------------------------------------------
sol = Solution()
print(sol.numberOfSpecialChars("aaAbcC"))    # Output: 2 (a/A, c/C)
print(sol.numberOfSpecialChars("aaAbcBC"))   # Output: 3 (a/A, b/B, c/C)
print(sol.numberOfSpecialChars("AbBCab"))    # Output: 0
print(sol.numberOfSpecialChars("aA"))        # Output: 1
