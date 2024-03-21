import random
import math
from bitarray import bitarray
alphabet = "abcdefghijklmnopqrstuvwxyz"

def create_random_string(str_len: str = 0) -> str:
    return "".join(random.choices(alphabet, k = str_len))

def encode(s: str = "") -> bitarray:
    l = len(s)
    minimum_len = math.ceil(math.log(26, 2) * l)
    num = 0
    for c in s:
        num = num * 26 + (ord(c) - ord("a"))
    encoded = bitarray(minimum_len)
    encoded.setall(0)
    for i in range(minimum_len):
        if num & (1 << (minimum_len - 1 - i)):
            encoded[i] = 1
    return encoded

def decode(encoded: bitarray = "") -> str:
    original = ""
    l = len(encoded)
    original_l = math.floor(l / math.log(26, 2))
    num = 0
    for i, digit in enumerate(encoded):
        num |= digit << (l-i-1)
    for i in range(original_l):
        original = chr(ord("a") + (num % 26)) + original
        num //= 26
    return original

def random_test(str_len: int = 0):
    original = create_random_string(str_len)
    encoded = encode(original)
    decoded = decode(encoded)
    assert original == decoded

def test_with_str(original: str = ""):
    encoded = encode(original)
    decoded = decode(encoded)
    assert original == decoded


for str_len in range(1, 101):
    print(f"my compression_rate for len {str_len}: {str_len * 8 / math.ceil(str_len * math.log(26, 2))}")
    for _ in range(50):
        random_test(str_len)
for str_len in [10**3, 10**4, 10**5]:
    print(f"my compression_rate for len {str_len}: {str_len * 8 / math.ceil(str_len * math.log(26, 2))}")
    random_test(str_len)


test_with_str("a") # encode_num = 0
test_with_str("aa") # encode_num = 0
test_with_str("aaa") # encode_num = 0
test_with_str("aab") # encode_num = 1
test_with_str("ab") # encode_num = 1
test_with_str("b") # encode_num = 1