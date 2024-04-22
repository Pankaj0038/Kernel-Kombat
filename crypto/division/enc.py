import binascii

flag = open('flag.txt').read()

def encode_base_2023(string):
    base = 2023
    encoded_value = 0

    for char in string:
        encoded_value = encoded_value * 2024 + ord(char)

    encoded_string = ""
    while encoded_value > 0:
        encoded_string = chr(encoded_value % base) + encoded_string
        encoded_value //= base

    return encoded_string

print(binascii.hexlify((encode_base_2023(flag)).encode()))

# enc : b'71c9b3c58cc5b1c9a8dcb3d0bc6fcd84ceb7d9a5dab4d296d9b2d194c88ad08cdba2caabcc8edab7deaad99bd9add6b2df95c3a3d5a6cc9adda1cdbac3a8cd9cd88537c5b9cc92dbaed490db91d1aacbbcc78ec986d085cc86de9dcca4cb93d390c695d48ec7bdd190ce83d896d681c6bdc2b0c5a9c7afdb9cd2875cd2a2c5b8c9a5ca87c9bdc5bdd28bd9aacfa5d7a9ddbddbacd18bccbacc94c6946ad68fdeb04bcd86cab9caa8d699c4aec489d7a6d2aa23c4bbc386c2abd39edfa2ce8ecab0d19ccf97deb1d785d9b0c3acd1b8c8a5da8bc288d0a7c489c985dbb3ca8fdeb9'
