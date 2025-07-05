from problems.longest_palindomic_substring import Solution
import pytest

def test_longest_palindomic_substring_babad():
    solution: Solution = Solution()
    test_string: str = 'babad'

    longest_palindrome: str = solution.longestPalindrome(test_string)
    assert any([longest_palindrome == 'bab', longest_palindrome == 'aba'])


def test_longest_palindomic_substring_cbbd():
    solution: Solution = Solution()
    test_string: str = 'cbbd'

    longest_palindrome: str = solution.longestPalindrome(test_string)
    assert longest_palindrome == 'bb'

def test_longest_palindomic_substring_bb():
    solution: Solution = Solution()
    test_string: str = 'bb'

    longest_palindrome: str = solution.longestPalindrome(test_string)
    assert longest_palindrome == 'bb'

def test_longest_palindomic_substring_ccc():
    solution: Solution = Solution()
    test_string: str = 'ccc'

    longest_palindrome: str = solution.longestPalindrome(test_string)
    assert longest_palindrome == 'ccc'

def test_longest_palindomic_substring_abcba():
    solution: Solution = Solution()
    test_string: str = 'abcba'

    longest_palindrome: str = solution.longestPalindrome(test_string)
    assert longest_palindrome == 'abcba'

def test_longest_palindomic_substring_abacab():
    solution: Solution = Solution()
    test_string: str = 'abacab'

    longest_palindrome: str = solution.longestPalindrome(test_string)
    assert longest_palindrome == 'bacab'
