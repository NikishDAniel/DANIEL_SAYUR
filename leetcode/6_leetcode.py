'''The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
 

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
Example 3:

Input: s = "A", numRows = 1
Output: "A"
'''


n = int(input())
s = 'PAYPALISHIRING'
result = ['']*n
count = 0
rowCount = 1
for i in s:
    if count == n:
        rowCount+=1
        count = 1
        result = list(reversed(result))
        result[count] += i
    else:
        result[count]+=i
    count += 1
result = result if rowCount %2 != 0 else list(reversed(result))
print(''.join(result))