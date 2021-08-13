class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        #take elements from cpdomains
        #split from 'space' charcter and create or add existing dict like this format dict[discuss.leetcode.com] = 9001
        #take the part which is comming from '.'
        #do it the same thing for it
        
        ans = collections.Counter()
        
        for cpdomain in cpdomains:
            count, domain = cpdomain.split()
            count = int(count)
            layers = domain.split(".")
            
            for i in range(len(layers)):
                key = ".".join(layers[i:])
                ans[key] += count
        return ["{} {}".format(count, domain) for domain, count in ans.items()]