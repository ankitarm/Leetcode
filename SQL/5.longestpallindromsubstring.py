class Solution:
  def longestPalindrome(self, s: str) -> str:
      # Helper function to expand around the center and find the length of the palindrome
      def expandAroundCenter(left: int, right: int) -> str:
          while left >= 0 and right < len(s) and s[left] == s[right]:
              left -= 1
              right += 1
          # return the palindrome found by expanding, s[left+1:right] since after the loop, the indices are out of bounds
          return s[left + 1:right]

      # If the input string is empty or has one character, it's already a palindrome
      if len(s) == 0:
          return ""

      longest = ""
      for i in range(len(s)):
          # Odd length palindromes
          odd_palindrome = expandAroundCenter(i, i)
          # Even length palindromes
          even_palindrome = expandAroundCenter(i, i + 1)

          # Update the longest palindrome found
          longest = max(longest, odd_palindrome, even_palindrome, key=len)
          if len(longest)==len(s):
              break

      return longest

if __name__ == '__main__':
    s = "abccba"
    solution = Solution()
    k = solution.longestPalindrome(s)
    print(k)