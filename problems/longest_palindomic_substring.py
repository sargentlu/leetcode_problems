from collections import deque

class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_substring: str = ''
        curr_chars: str
        curr_substring: str
        center: str

        i: int; l: int; r: int
        char: str
        for i, char in enumerate(s):
            curr_chars = ''
            r = 1

            while True:
                if not(i + r < len(s) and s[i + r] == char):
                    break

                r += 1

            center = r * char
            l = i - 1 # l is now at the left of center start
            r += i # r is now at the right of center end

            while True:
                if l < 0 or r >= len(s) or s[l] != s[r]:
                    break

                curr_chars += s[r]
                l -= 1
                r += 1

            if len(center) + 2 * len(curr_chars) > len(longest_substring):
                longest_substring = self.palindrome_string(center, curr_chars)

        return longest_substring


    @staticmethod
    def palindrome_string(center: str, substring: str = None) -> str:
        if not substring:
            return center
        elif len(substring) == 1:
            return substring + center + substring

        return substring[::-1] + center + substring
