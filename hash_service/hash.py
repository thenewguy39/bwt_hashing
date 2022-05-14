"""""

n -> no. of bits 

doc -> document to be encoded

arr -> store index values

secret -> secret key value

Functions:

convert(doc) function -> returns document converted to binary
    "a bc" -> "110000100101001100010110001011"

get(doc) function -> returns the next input string

bwt(string) function -> returns (output string, index) 

"""""

from .services import Services


class Hash:
    def compute(self, doc, n):
        services = Services(n)
        #doc = services.convertBinary(doc)
        key = services.generateKey()
        s = ""
        pointer = 0
        indexArr = []

        while(pointer != len(doc)):
            s = services.get(doc, pointer)
            pointer += n

            temp = services.XOR(s, key)
            index, s = services.bwt(temp)

            indexArr.append(index)
            key = s

        return s
