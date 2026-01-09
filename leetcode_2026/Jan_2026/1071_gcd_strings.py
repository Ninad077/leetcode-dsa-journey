class Solution(object):
    def gcdOfStrings(self, str1, str2):
        # If concatenation property fails, no common divisor string
        if str1 + str2 != str2 + str1:
            return ""
        
        else:
            a = len(str1) 
            b = len(str2)

            while b!= 0: