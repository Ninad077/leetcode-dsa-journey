class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """

        output_list = []
        i = 0
        for i in range(len(candies)):
            output = candies[i] + extraCandies
            if output >= max(candies):
                output_list.append(True)
            else:
                output_list.append(False)
        i += 1

        return output_list