class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = "" #5 Hello5 World
        for i in range(len(strs)):
            tmp = len(strs[i])
            tmp = str(tmp)
            tmp_encode = tmp + " " + strs[i]
            encoded += tmp_encode
        
        return encoded

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            tmp = ""
            j = s.find(" ", i)
            length = int(s[i:j])
            tmp = s[j + 1:j + length + 1]
            i = j + length + 1
            result.append(tmp)
        return result




