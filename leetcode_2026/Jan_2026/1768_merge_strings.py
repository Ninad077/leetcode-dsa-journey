class Solution(object):
    def mergeAlternately(self, word1, word2):
        list_eg1 = []
        i = 0

        while i < len(word1) or i < len(word2):
            if i < len(word1):
                list_eg1.append(word1[i])
            if i < len(word2):
                list_eg1.append(word2[i])
            i += 1
        return "".join(list_eg1)
        