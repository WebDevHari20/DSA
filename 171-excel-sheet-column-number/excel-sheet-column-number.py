class Solution(object):
    def titleToNumber(self, columnTitle):
        result = 0;
        n = columnTitle
        for i in n:
            result = result*26+(ord(i)-ord("A")+1)
        return result