class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        s=s[::-1]
        c=0
        for i in s:
            if(i!=" "):c+=1
            else:break
        return c
