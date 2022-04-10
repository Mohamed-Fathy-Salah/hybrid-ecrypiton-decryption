from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def generate_key():
    key = RSA.generate(2048)

    public_key = key.publickey().exportKey('PEM')
    with open("generated/public_key", "wb") as f:
        f.write(public_key)
        f.close()

    private_key = key.export_key('PEM')
    with open("generated/private_key", "wb") as f:
        f.write(private_key)
        f.close()

def encrypt(text, key_file):
    with open(key_file, "r") as f:
        public_key = f.read()
        f.close()

    rsa_public_key = RSA.importKey(public_key)
    rsa_public_key = PKCS1_OAEP.new(rsa_public_key)
    encrypted_text = rsa_public_key.encrypt(text)

    with open("encrypted/AES_key.enc", "wb") as f:
        f.write(encrypted_text)
        f.close()

def decrypt(text_file, key_file):
    with open(text_file, "rb") as f:
        text = f.read()
        f.close()
    
    with open(key_file, "r") as f:
        private_key = f.read()
        f.close()

    rsa_private_key = RSA.importKey(private_key)
    rsa_private_key = PKCS1_OAEP.new(rsa_private_key)
    decrypted_text = rsa_private_key.decrypt(text)
    

    decrypted_file = text_file.removesuffix('.enc')
    decrypted_file = decrypted_file.split("/")[-1]
    with open("decrypted/{}".format(decrypted_file), "wb") as f:
        f.write(decrypted_text)
        f.close()

    return decrypted_text
