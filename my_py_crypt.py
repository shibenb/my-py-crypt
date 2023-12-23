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

import my_py_crypt_lib

if cmd == "ek":
    print("impl key based enc")
    #key = create_and_load_key(token)
    #encrypt(file, token)
elif cmd == "dk":
    print("impl key based dec")
    #key = load_key(token)
    #decrypt(file, key)
elif cmd == "ep":
    if token == "stdin":
        token = input("Password: ")
        token2 = input("Again: ")
        if token != token2:
            print("Passwords don't match")
            break
    print("impl password based enc: " + token)
elif cmd == "dp":
    if token == "stdin":
        token = input("Password: ")
    print("impl password based dec: " + token)
else:
    print("Invalid Command")

del my_py_crypt_lib
