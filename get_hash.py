from hash_service import hash

doc = input()
n = 8
print("Hash key is " + hash.compute(doc, n))
