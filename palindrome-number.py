# Given an integer x, return true if x is a palindrome, and false otherwise.

def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        return str(x) == str(x)[::-1]