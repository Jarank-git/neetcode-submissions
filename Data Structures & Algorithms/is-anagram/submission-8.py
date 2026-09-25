class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            count_1 = {}
            count_2 = {}
            cnt = 0
            for c in s:
                count_1[c] = count_1.get(s[cnt], 0) + 1
                cnt +=1 
            cnt = 0   
            for i in t:
                count_2[i] = count_2.get(t[cnt], 0) + 1
                cnt +=1
            
            for j in count_1:
                if count_1.get(j,0) != count_2.get(j,0): 
                    return False   
            return True


            