'''Given an integer n, return the number of prime numbers that are strictly less than n.

 

Example 1:

Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
Example 2:

Input: n = 0
Output: 0
Example 3:

Input: n = 1
Output: 0
 

Constraints:

0 <= n <= 5 * 106'''

class Solution:
    def countPrimes(self, n: int) -> int:
        '''count = 0
        for i in range(2,n):
            for j in range(2,i):
                if i%j == 0 and i!=j:
                    break
                else:
                    continue
            else:
                count += 1
        return count'''
        numbers = [True for x in range(n+1)]
        index = 2
        while index*index <= n:
            if numbers[index] == True:
                for i in range(index*index,n+1,index):
                    numbers[i] = False
            index += 1
        result = [x for x in range(2,n) if numbers[x]]
        return len(result)