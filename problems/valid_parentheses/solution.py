class Solution:
    def isValid(self, s: str) -> bool:
        """bracketsOpen = ["(", "[", "{"]
        bracketsClose = [")", "]", "}"]
        Flag = True
        open_indexs = []
        for i in s:
            if i in bracketsOpen:
                open_indexs.append(bracketsOpen.index(i))
                print(open_indexs)
            else:
                for index in range(len(open_indexs)-1, -1, -1):
                    if i != bracketsClose[index]:
                        print(Flag)
                        Flag = False
                open_indexs = []
        return Flag"""
    
        dic = {"(":")", "[":"]", "{":"}"}
        Flag = True
        stacks = []
        for i in s:
            if i in dic.keys():
                stacks.append(i)
            else:
                if i in dic.values():
                    if (stacks == []) or (i != dic[stacks.pop()]):
                        return False
                else:
                    return False
        return stacks == []