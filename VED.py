"""
video encryption / decryption driver
"""
import argparse
from sys import argv
import RSA
import AES

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument("-t", "--type", type=int, help="0: KeyPair generation(default)\n1: Encryption\n2: Decryption", default=0)
    ap.add_argument("-v", "--video", type=str, help="Video file name to be encrypted / decrypted")
    ap.add_argument("-a", "--AES_key", type=str, help="Encrypted AES key file name")
    ap.add_argument("-r", "--RSA_key", type=str, help="RSA key file name (public -> encryption/ private -> decryption)")
    args = ap.parse_args(argv[1:])

    if args.type == 0:
        RSA.generate_key()
    elif args.type == 1:
        if(args.video == None):
            print("type `python VED.py -h` for help")
            exit()

        AES.encrypt(args.video, args.RSA_key)
    elif args.type == 2:
        if(args.video == None or args.AES_key == None or args.RSA_key == None):
            print("type `python VED.py -h` for help")
            exit()

        AES.decrypt(args.video, args.AES_key, args.RSA_key)
    else:
        print("type `python VED.py -h` for help")

