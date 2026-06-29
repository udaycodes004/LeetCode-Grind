class Solution:
    def maxArea(self, height: List[int]) -> int:
        n=len(height)
        l=0
        r=n-1
        mvol=0
        while(l<r):
            ht=min(height[l],height[r])
            wd=r-l
            vol=ht*wd
            mvol=max(vol,mvol)
            if(height[l]<=height[r]):
                l+=1
            else:
                r-=1
        return mvol
            

        