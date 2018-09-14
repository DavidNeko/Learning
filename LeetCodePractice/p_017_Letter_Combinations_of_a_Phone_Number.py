#coding = utf-8
"""
[Difficulty : Medium]

Given a string containing digits from 2-9 inclusive, return all
possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons)
is given below. Note that 1 does not map to any letters.

num_dict = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
            }

Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

Note:
    Although the above answer is in lexicographical order, your answer
    could be in any order you want.

"""

class Solution(object):

    def __init__(self):
        # init global vars
        self.num_dict= {
                    "2" : "abc",
                    "3" : "def",
                    "4" : "ghi",
                    "5" : "jkl",
                    "6" : "mno",
                    "7" : "pqrs",
                    "8" : "tuv",
                    "9" : "wxyz"
                    }

        self.result = []


    def letterCombinations(self, string):
        """
        :type string: str
        :rtype: List[str]
        """

        # handle certain conditions
        # if string is empty
        if not string:
            return []

        # helper function
        # depth first search
        def dfs(string, index, temp):
            # add temp to result if length of input array equals to temp
            if len(string) == len(temp):
                self.result.append("".join(temp)) # or join(x for x in temp)
                return

            for char in self.num_dict[string[index]]:
                temp.append(char)
                dfs(string, index+1, temp)
                temp.pop()


        # function call
        dfs(string, 0, [])


    def test(self):
        self.letterCombinations("23")
        print self.result
        print ""
