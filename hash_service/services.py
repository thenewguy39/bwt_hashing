import random


class Services:
    def __init__(self, n):
        self.n = n

    def convertBinary(self, doc):
        res = ''.join(format(ord(i), '0'+str(self.n)+'b') for i in doc)
        return res

    def XOR(self, s1, s2):
        ans = ""
        for i in range(len(s1)):
            if (s1[i] == s2[i]):
                ans += "0"
            else:
                ans += "1"
        return ans

    def bwt(self, s):
        n = len(s)
        m = sorted([s[i:n]+s[0:i] for i in range(n)])
        I = m.index(s)
        L = ''.join([q[-1] for q in m])

        return (I, L)

    def generateKey(self):
        key = ""
        for i in range(self.n):
            key += str(random.randint(0, 1))
        return key

    def get(self, doc, pointer):
        if(pointer == len(doc)):
            return ""

        output = doc[pointer: pointer + self.n]
        return output
