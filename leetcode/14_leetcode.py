'''Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.'''

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        stri = sorted(strs,key=lambda x:len(x))
        def check(x,y):
            for i in stri[1:]:
                if y == i[x]:
                    continue
                else:
                    return ''
            return y            
        if len(stri)>1:
            result = ''
            first = stri[0]
            for i,z in enumerate(first):
                if check(i,z)!='':
                    result += z  
                else:
                    break
            return result
        else:
            return stri[0]