class Solution:
    # I can only think of the most common way of using non-ascii characters.
    # The hints use length(digits) + #, which I couldn't think of
    def encode(self, strs: List[str]) -> str:
        for i in range(len(strs)):
            s = strs[i]
            length = len(s)
            strs[i] = str(length)+'#'+s
        return ''.join(strs)
    def decode(self, s: str) -> List[str]:
        i = 0
        l = []
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            l.append(s[j+1:j+length+1])
            i = j+length+1
        return l