# import argparse
# from sys import argv
import RSA
import AES

# RSA.generate_key()
# AES.encrypt("a.mp4", "public_key")
AES.decrypt("a.mp4.enc", "AES_key.enc", "private_key")

# if __name__ == '__main__':
    # ap = argparse.ArgumentParser()
    # ap.add_argument("-d", "--decrypt", type=int, help="1 for decryption(default)\nany other number for encryption", default=1)
    # ap.add_argument("-t", "--text", type=str, help="text to be encrypted / decrypted", required=True)
    # ap.add_argument("-k", "--key", type=str, help="key used for encryption / decryption", required=True)
    # args = ap.parse_args(argv[1:])

    # if args.decrypt == 1:
        # print(AES.decrypt(args.text, args.key))
    # else:
        # print(AES.encrypt(args.text, args.key))

