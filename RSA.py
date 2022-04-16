from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import os

def generate_key():
    key = RSA.generate(2048)

    public_key = key.publickey().exportKey('PEM')
    public_key_file = os.path.join("generated", "public_key")
    with open(public_key_file, "wb") as f:
        f.write(public_key)

    private_key = key.export_key('PEM')
    private_key_file = os.path.join("generated", "private_key")
    with open(private_key_file, "wb") as f:
        f.write(private_key)

def encrypt(text, public_key_file):
    with open(public_key_file, "r") as f:
        public_key = f.read()

    rsa_public_key = RSA.importKey(public_key)
    rsa_public_key = PKCS1_OAEP.new(rsa_public_key)
    encrypted_text = rsa_public_key.encrypt(text)

    encrypted_file = os.path.join("encrypted", "AES_key.enc")
    with open(encrypted_file, "wb") as f:
        f.write(encrypted_text)

def decrypt(text_file, private_key_file):
    with open(text_file, "rb") as f:
        text = f.read()
    
    with open(private_key_file, "rb") as f:
        private_key = f.read()

    rsa_private_key = RSA.importKey(private_key)
    rsa_private_key = PKCS1_OAEP.new(rsa_private_key)
    decrypted_text = rsa_private_key.decrypt(text)
    
    decrypted_file = os.path.join("decrypted", os.path.basename(text_file).removesuffix(".enc"))
    with open(decrypted_file, "wb") as f:
        f.write(decrypted_text)

    return decrypted_text
