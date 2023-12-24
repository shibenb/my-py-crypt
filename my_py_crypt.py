#!/usr/bin/python3

arg_desc = "File encryption or decryption tool with key or key + password."

arg_command = "command"
arg_command_help = "encrypt | decrypt"

arg_infile = "infile"
arg_infile_help = "Input file to be encrypted or decrypted."

arg_keyfile = "-k"
arg_keyfile_major = "--keyfile"
arg_keyfile_help = "Key file to be used for encryption (will be created) or decryption (should be provided) of your input file. If argument not provided, then a file with an added extention of \"key\" will be assumed."

arg_password = "-p"
arg_password_major = "--password"
arg_password_help = "Ask for password to accompany the key. If argument not provided, the file will be encrypted or decrypted with only the key. If a file was encrypted with password, then the same passwod must be provided to decrypt it."

arg_outfile = "-o"
arg_outfile_major = "--outfile"
arg_outfile_help = "Resultant file of encryption or decryption. If argument not provided, a file with the same name as the input file, with an appropriate added extention, will be created."

import argparse
parser = argparse.ArgumentParser(description=arg_desc)
parser.add_argument(arg_command, help=arg_command_help)
parser.add_argument(arg_infile, help=arg_infile_help)
parser.add_argument(arg_keyfile, arg_keyfile_major, help=arg_keyfile_help)
parser.add_argument(arg_password, arg_password_major, help=arg_password_help, action="store_true")
parser.add_argument(arg_outfile, arg_outfile_major, help=arg_outfile_help)

args = parser.parse_args()
command = args.command
infile = args.infile
keyfile = args.keyfile
password = args.password
outfile = args.outfile

del argparse

import getpass
import my_py_crypt_lib

if command == "encrypt":
    if password:
        pass1 = getpass.getpass("Password: ")
        pass2 = getpass.getpass("Again: ")
        if pass1 != pass2:
            print("Passwords don't match")
            exit(1)
        else:
            key = my_py_crypt_lib.generate_key_and_salt(keyfile, pass1)
            my_py_crypt_lib.encrypt(infile, key)
    else:
        key = my_py_crypt_lib.create_and_load_key(keyfile)
        my_py_crypt_lib.encrypt(infile, key)
elif command == "decrypt":
    if password:
        pass1 = getpass.getpass("Password: ")
        key = my_py_crypt_lib.generate_key_with_salt(keyfile, pass1)
        my_py_crypt_lib.decrypt(infile, key)
    else:
        key = my_py_crypt_lib.load_key(keyfile)
        my_py_crypt_lib.decrypt(infile, key)
else:
    print("Invalid Command")
