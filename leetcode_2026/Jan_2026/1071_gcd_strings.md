Question
For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

 

Example 1:

Input: str1 = "ABCABC", str2 = "ABC"

Output: "ABC"

Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"

Output: "AB"

Example 3:

Input: str1 = "LEET", str2 = "CODE"

Output: ""

Example 4:

Input: str1 = "AAAAAB", str2 = "AAA"

Output: ""

______________________________________________________________________________________________________
Logic: 
if the concat of str1 and str2 is not the same from end to end print null,
else just use gcd logic:
say

str1 = 'ABCABC'
str2 = 'ABC'

a= len(str1) = 6
b = len(str2) = 3

6,3 = 3, (6%3)
3, 0
remainder 0, loop breaks (since b!=0)
so here a= 3, so fincal value gets stored in 'a' always

Then we slice it till the range of a (str1[:a]) which means from 0 postion till '3' postion.  
str1[:3] => ABC