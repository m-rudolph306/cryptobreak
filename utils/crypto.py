from Crypto.Cipher import AES

def aes_cbc_encrypt(plaintext: bytes, key: bytes, iv: bytes) -> bytes:
    cipher = AES.new(key, AES.MODE_ECB)
    previous = iv
    result = b""
    blocks = len(plaintext) // 16 
    for i in range(0,blocks):
        block = plaintext[i*16:(i+1)*16]
        xored = bytes(a ^ b for a, b in zip(block, previous))
        previous = cipher.encrypt(xored)
        result += previous 
    return result  # verschlüsselt genau 16 Bytes 

def aes_cbc_decrypt(ciphertext: bytes, key: bytes, iv: bytes) -> bytes:
    cipher = AES.new(key, AES.MODE_ECB)
    previous = iv 
    result = b""
    blocks = len(ciphertext) // 16
    for i in range(0, blocks):
        block = ciphertext[i*16:(i+1)*16]
        decrypted = cipher.decrypt(block)
        xored = bytes(a ^ b for a, b in zip(decrypted, previous))
        result += xored
        previous = block
    return result 

def pkcs7_pad(data: bytes, block_size: int):
    length_data = len(data)
    padding_needed = block_size - (length_data % block_size)
    for _ in range(0,padding_needed):
        data += bytes([padding_needed])
    return data

print(pkcs7_pad(b"YELLOW SUBMARINE", 20))
# Erwartet: b"YELLOW SUBMARINE\x04\x04\x04\x04"

print(pkcs7_pad(b"YELLOW SUBMARINE", 16))
# Erwartet: b"YELLOW SUBMARINE\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10"

key = b"YELLOW SUBMARINE"
iv = b"\x04" * 16
plaintext = pkcs7_pad(b"hello world!!!!!", 16)
ciphertext = aes_cbc_encrypt(plaintext, key, iv)
assert aes_cbc_decrypt(ciphertext, key, iv) == plaintext
print("works")
