## 1431. Kids With the Greatest Number of Candies
-------------------------------------------------------------------------------------
There are n kids with candies. You are given an integer array candies, where each candies[i] represents the number of candies the ith kid has, and an integer extraCandies, denoting the number of extra candies that you have.

Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies, they will have the greatest number of candies among all the kids, or false otherwise.

Note that multiple kids can have the greatest number of candies.

E.g.

Input: candies = [2,3,5,1,3], extraCandies = 3

Output: [true,true,true,false,true] 

-------------------------------------------------------------------------------------

Solution:

### Function wrapper

    def kidsWithCandies(self, candies, extraCandies):

### Preparing empty o/p list & initialising the index
        output_list = []
        i = 0

### Looping it through the list & compare it with the max number in the list

        for i in range(len(candies)):
            output = candies[i] + extraCandies
            if output >= max(candies):
                output_list.append(True)
            else:
                output_list.append(False)
        i += 1 

### Return the o/p
        return output_list






