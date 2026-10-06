class Solution:
    def isPalindrome(self, s: str) -> bool:
        pointer1 = ""
        pointer2 = ""
        total_length = len(s)

        lean_string = (re.sub(r'[^a-zA-Z0-9]', '', s))
        total_length = len(lean_string)
        lower_case = lean_string.lower()


        for i in range(len(lean_string)):
            pointer1 = lower_case[i]
            pointer2 = lower_case[total_length - i - 1]
            if pointer1 != pointer2:
                return False

        return True
        