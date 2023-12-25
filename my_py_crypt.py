#!/usr/bin/python3

arg_desc = 'File encryption or decryption tool with key or along with a password.'

arg_command = 'command'
arg_command_help = 'encrypt | decrypt'

arg_infile = 'infile'
arg_infile_help = 'Input file to be encrypted or decrypted.'

arg_keyfile = '-k'
arg_keyfile_major = '--keyfile'
arg_keyfile_help = 'Key file to use for encryption or decryption of the Input file. If does not exist, then will be created when encrypting. An existing key file is required when decrypting. Key is called \"salt\" when pairing with a password. If argument not provided, then a file with the same name as infile, with an added appropriate extention, will be assumed as an argument.'

arg_password = '-p'
arg_password_major = '--password'
arg_password_help = 'Create a password to pair with the key (salt) in case of encryption. Provide an existing password paired with the key (salt) for decryption. If argument not provided, the file will be encrypted or decrypted with only the keyfile. If a file was encrypted with password, then the same passwod must be provided to decrypt it.'

arg_outfile = '-o'
arg_outfile_major = '--outfile'
arg_outfile_help = 'Resultant file of encryption or decryption. If argument not provided, then a file with the same name as infile, with an added appropriate added extention, will be assumed as an argument.'

import argparse
parser = argparse.ArgumentParser(description=arg_desc)
parser.add_argument(arg_command, help=arg_command_help)
parser.add_argument(arg_infile, help=arg_infile_help)
parser.add_argument(arg_keyfile, arg_keyfile_major, help=arg_keyfile_help)
parser.add_argument(arg_password, arg_password_major, help=arg_password_help, action='store_true')
parser.add_argument(arg_outfile, arg_outfile_major, help=arg_outfile_help)
args = parser.parse_args()

import my_py_crypt_utils

if args.command == 'encrypt':
    if args.password:
        my_py_crypt_utils.encrypt_with_sap(args.infile, args.keyfile, args.outfile)
    else:
        my_py_crypt_utils.encrypt_with_key(args.infile, args.keyfile, args.outfile)
elif args.command == 'decrypt':
    if args.password:
        my_py_crypt_utils.decrypt_with_sap(args.infile, args.keyfile, args.outfile)
    else:
        my_py_crypt_utils.decrypt_with_key(args.infile, args.keyfile, args.outfile)
else:
    import sys
    sys.stderr.write(f'Error: Invalid Command. Only \"encrypt\" or \"decrypt\" is accepted.\n')
