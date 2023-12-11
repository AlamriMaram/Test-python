class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        reversed_n = 0
        temp = x

        while temp != 0:
            digit = temp % 10
            reversed_n = reversed_n * 10 + digit
            temp //= 10

        return reversed_n == x