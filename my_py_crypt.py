#!/usr/bin/python3

arg_desc = "File encryption/decryption tool with key/password"
arg_cmd = "cmd"
arg_cmd_help = "ek (encrypt with key file) | dk (decrypt with key file) | ep (encrypt with password) | dp (decrypt with password)"
arg_file = "file"
arg_file_help = "File to be encrypted or decrypted"
arg_token = "token"
arg_token_help = "key file to use if cmd=ek|dk, password to use if cmd=ep|dp. Password will be asked as input if provided as \"stdin\" (without quotes)"

import argparse
parser = argparse.ArgumentParser(description=arg_desc)
parser.add_argument(arg_cmd, help=arg_cmd_help)
parser.add_argument(arg_file, help=arg_file_help)
parser.add_argument(arg_token, help=arg_token_help)

args = parser.parse_args()
cmd = args.cmd
file = args.file
token = args.token

del argparse

import getpass
import my_py_crypt_lib

if cmd == "ek":
    key = my_py_crypt_lib.create_and_load_key(token)
    my_py_crypt_lib.encrypt(file, key)
elif cmd == "dk":
    key = my_py_crypt_lib.load_key(token)
    my_py_crypt_lib.decrypt(file, key)
elif cmd == "ep":
    if token == "stdin":
        token = getpass.getpass("Password: ")
        token2 = getpass.getpass("Again: ")
        if token != token2:
            print("Passwords don't match")
            exit(1) #return
    key = my_py_crypt_lib.generate_key(token)
    my_py_crypt_lib.encrypt(file, key)
elif cmd == "dp":
    if token == "stdin":
        token = getpass.getpass("Password: ")
    key = my_py_crypt_lib.generate_key(token)
    my_py_crypt_lib.decrypt(file, key)
else:
    print("Invalid Command")
