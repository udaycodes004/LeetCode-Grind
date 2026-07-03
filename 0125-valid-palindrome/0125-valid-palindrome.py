class Solution:
    def isPalindrome(self, s: str) -> bool:
        str2=''
        for i in s:
            if i.isalnum():
                str2+=i.lower()
        return (str2==str2[::-1])
        