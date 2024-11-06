from hashtables import HashTable

ht = HashTable()
ht.put("cat", "A furry animal which goes meow")
ht.put("dog", "A furry animal which goes woof")


print(ht.get("cat")) # A furry animal which goes meow
print(ht.get("dog")) # A furry animal which goes woof