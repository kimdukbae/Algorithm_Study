import hashlib


# 해시 함수 생성
def sha1_hash(input_str):
    hash_obj = hashlib.sha1(input_str.encode())
    hash_value = hash_obj.hexdigest()

    return hash_value


hash_value_apple = sha1_hash('Apple')
print(hash_value_apple)
print(len(hash_value_apple))

print()

hash_value_banana = sha1_hash('Banana')
print(hash_value_banana)
print(len(hash_value_banana))

print()

hash_value_melon = sha1_hash('Melon')
print(hash_value_melon)
print(len(hash_value_melon))
print()

hash_value_strawberry = sha1_hash('Strawberry')
print(hash_value_strawberry)
print(len(hash_value_strawberry))
