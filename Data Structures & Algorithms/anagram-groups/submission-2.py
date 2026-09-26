class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        cnt = {}
        for i in range (len(strs)):
            #create key by sorted each word in list alphabetically
            label = "".join(sorted(strs[i]))
            #if label exists in hashmap, then take the sublist and append the current word
            if label in cnt:
                cnt[label].append(strs[i])
            #if label does not exist in hashmap, then create a new list with the initial value
            else:
                cnt[label] = [strs[i]]

        return list(cnt.values())


        