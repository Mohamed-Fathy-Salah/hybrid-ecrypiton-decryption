from Crypto.Cipher import AES
from secrets import token_bytes
import RSA
import os

def encrypt(text_file, RSA_public_key_file):
    key = token_bytes(16)
    RSA.encrypt(key, RSA_public_key_file)

    model = AES.new(key, AES.MODE_GCM, nonce=b'0')

    with open(text_file, 'rb') as f:
        plain_text = f.read()

    encrypted_text = model.encrypt(plain_text)

    encrypted_file = os.path.join("encrypted", f"{os.path.basename(text_file)}.enc")
    with open(encrypted_file, 'wb') as f:
        f.write(encrypted_text)

def decrypt(encrypted_file, AES_key_file, RSA_private_key_file):
    key = RSA.decrypt(AES_key_file, RSA_private_key_file)
    model = AES.new(key, AES.MODE_GCM, nonce=b'0')

    with open(encrypted_file, 'rb') as f:
        encrypted_text = f.read()
    decrypted_text = model.decrypt(encrypted_text)

    decrypted_file = os.path.join("decrypted", os.path.basename(encrypted_file).removesuffix(".enc"))
    with open(decrypted_file, 'wb') as f:
        f.write(decrypted_text)

