'''Given an integer numRows, return the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]'''

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        listr = [[1],[1,1]]
        for i in range(2,numRows):
            prev = listr[i-1]
            new = [prev[i]+prev[i+1] for i in range(len(prev)-1)]
            new.insert(0,1)
            new.insert(i,1)
            listr.append(new)
        return listr