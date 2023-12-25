#!/usr/bin/python3

arg_desc = "File encryption or decryption tool with key or along with a password."

arg_command = "command"
arg_command_help = "encrypt | decrypt"

arg_infile = "infile"
arg_infile_help = "Input file to be encrypted or decrypted."

arg_keyfile = "-k"
arg_keyfile_major = "--keyfile"
arg_keyfile_help = "Key file with this name will be created in case of encryption. An existing key file is required for decryption. If argument not provided, then a file with the same name as infile, with an added appropriate extention, will be assumed as an argument."

arg_password = "-p"
arg_password_major = "--password"
arg_password_help = "Will ask to create a password to pair with the key (named \"salt\") in case of encryption. Will ask an existing password is required for decryption. If argument not provided, the file will be encrypted or decrypted with only the keyfile. If a file was encrypted with password, then the same passwod must be provided to decrypt it."

arg_outfile = "-o"
arg_outfile_major = "--outfile"
arg_outfile_help = "Resultant file of encryption or decryption. If argument not provided, then a file with the same name as infile, with an added appropriate added extention, will be created."

import argparse
parser = argparse.ArgumentParser(description=arg_desc)
parser.add_argument(arg_command, help=arg_command_help)
parser.add_argument(arg_infile, help=arg_infile_help)
parser.add_argument(arg_keyfile, arg_keyfile_major, help=arg_keyfile_help)
parser.add_argument(arg_password, arg_password_major, help=arg_password_help, action="store_true")
parser.add_argument(arg_outfile, arg_outfile_major, help=arg_outfile_help)

args = parser.parse_args()

import getpass
import my_py_crypt_lib

if args.command == "encrypt":
    if args.password:
        pass1 = getpass.getpass("Password: ")
        pass2 = getpass.getpass("Again: ")
        if pass1 != pass2:
            print("Passwords don't match")
            exit(1)
        else:
            key = my_py_crypt_lib.generate_key_and_salt(args.keyfile, pass1)
            my_py_crypt_lib.encrypt(args.infile, key)
    else:
        key = my_py_crypt_lib.create_and_load_key(args.keyfile)
        my_py_crypt_lib.encrypt(args.infile, key)
elif args.command == "decrypt":
    if args.password:
        pass1 = getpass.getpass("Password: ")
        key = my_py_crypt_lib.generate_key_with_salt(args.keyfile, pass1)
        my_py_crypt_lib.decrypt(args.infile, key)
    else:
        key = my_py_crypt_lib.load_key(args.keyfile)
        my_py_crypt_lib.decrypt(args.infile, key)
else:
    print("Invalid Command")
