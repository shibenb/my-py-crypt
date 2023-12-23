arg_desc = "File encryption/decryption tool with key/password"
arg_cmd = "cmd"
arg_cmd_help = "ek (encrypt with key file) | dk (decrypt with key file) | ep (encrypt with password) | dp (decrypt with password)"
arg_file = "file"
arg_file_help = "File to be encrypted or decrypted"
arg_key = "token"
arg_key_help = "key file to use if cmd=ek|dk, password to use if cmd=ep|dp. Password will be asked as input if not provided"

import argparse
parser = argparse.ArgumentParser(description=)
parser.add_argument(arg_cmd, help=arg_cmd_help)
parser.add_argument(arg_file, help=arg_file_help)
parser.add_argument(arg_key, help=arg_key_help)

args = parser.parse_args()
cmd = args.cmd
file = args.file
token = args.token

del argparse

import mypycryptlib

if cmd = "ek":
    create_key(arg_key)
    encrypt(file, arg_key)
elif cmd = "ep":
    

