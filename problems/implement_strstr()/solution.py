class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """if len(haystack) + len(needle) == 0:
            return 0
        index_haystack = 0
        index_needle = 0
        check = 0
        flag = False
        
        while (index_haystack < len(haystack)):
            print("index haystack:", index_haystack)
            while (index_needle < len(needle)):
                print("index needle:", index_needle)
                if (haystack[index_haystack] != needle[index_needle]):
                    index_haystack += 1
                    index_needle = 0
                else:
                    index_haystack += 1
                    index_needle += 1
                    check += 1
                    if check == len(needle):
                        return index_haystack - index_needle
                #index_needle += 1
            #index_haystack += 1
        return -1
        """
        return haystack.find(needle)