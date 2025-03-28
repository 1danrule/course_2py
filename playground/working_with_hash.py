import hashlib

data = "1glk;jhjifgjhgoujfji             hgiufgihufgoiuhifg1їїї".encode()
print(data)

hash_value = hashlib.sha256(data).hexdigest()
print(hash_value)


hash_value = hashlib.md5(data).hexdigest()
print(hash_value)