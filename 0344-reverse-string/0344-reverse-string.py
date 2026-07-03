class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n=len(s)
        left=0
        right=n-1
        while(left<=right):
            s[right],s[left]=s[left],s[right]
            right-=1
            left+=1
            