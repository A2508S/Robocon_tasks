class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dictionary = {"(": ")", "[": "]", "{": "}"}
        a = []
        if len(s)<2 or len(s)%2 != 0 or s[0] in ')}]':
            return False
        else:
            for i in s:
                if i in dictionary.keys():
                    a.append(i)
                else:
                    if len(a) != 0:
                        if dictionary[a.pop()] != i:
                            return False
                    else:
                        return False
        return len(a) == 0
