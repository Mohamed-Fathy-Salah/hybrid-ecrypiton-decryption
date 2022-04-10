from Crypto.Cipher import AES
from secrets import token_bytes
import RSA

def encrypt(video_file, RSA_public_key_file):
    key = token_bytes(16)
    RSA.encrypt(key, RSA_public_key_file)

    model = AES.new(key, AES.MODE_EAX, nonce=b'0')

    with open(video_file, 'rb') as f:
        plain_text = f.read()
        f.close();

    encrypted_text = model.encrypt(plain_text)

    video_file = video_file.split("/")[-1] 
    with open("encrypted/{}.enc".format(video_file), 'wb') as f:
        f.write(encrypted_text)
        f.close()

def decrypt(encrypted_video_file, AES_key_file, RSA_private_key_file):
    key = RSA.decrypt(AES_key_file, RSA_private_key_file)
    model = AES.new(key, AES.MODE_EAX, nonce=b'0')

    with open(encrypted_video_file, 'rb') as f:
        encrypted_text = f.read()
    decrypted_text = model.decrypt(encrypted_text)

    decrypted_video_file = encrypted_video_file.removesuffix('.enc')
    decrypted_video_file = decrypted_video_file.split("/")[-1]
    with open("decrypted/{}".format(decrypted_video_file), 'wb') as f:
        f.write(decrypted_text)

