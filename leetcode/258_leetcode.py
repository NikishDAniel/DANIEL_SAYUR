'''Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

Example 1:
Input: num = 38
Output: 2
Explanation: The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2 
Since 2 has only one digit, return it.

Example 2:
Input: num = 0
Output: 0

Constraints:

0 <= num <= 231 - 1'''

class Solution:
    def addDigits(self, num: int) -> int:
        output1 = 0
        def get(num):
            numstr = str(num)
            num = 0
            for i in numstr:
                num+=int(i)
            return num
        if num <= 9:
            return num
        else:
            while num>9:
                output1 = get(num)
                num = output1
                if output1<10:
                    break
            return output1