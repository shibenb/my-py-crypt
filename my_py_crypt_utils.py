import os
import sys

enc_ext='.encrypted'
dec_ext='.decrypted'
key_ext='.key'
salt_ext='.salt'

def is_directory_writable(directory_path):
    try:
        test = os.access(directory_path, os.W_OK)
        return True
    except (TypeError, PermissionError):
        return False

def encryption_preparation(infile, mutables, ext):
    if not os.access(infile, os.F_OK & os.R_OK):
        sys.stderr.write(f"Error: Cannot open input file [{infile}].\n")
        return False

    if infile.endswith(dec_ext):
        infile = infile[: -len(dec_ext)]
    if not mutables['outfile']:
        mutables['outfile'] = infile + enc_ext
        sys.stdout.write(f"Assuming Output file [{mutables['outfile']}].\n")
    if not mutables['keyfile']:
        mutables['keyfile'] = infile + ext
        sys.stdout.write(f"Assuming Key file [{mutables['keyfile']}].\n")

    if os.path.exists(mutables['outfile']):
        sys.stderr.write(f"Error: Output file [{mutables['outfile']}] already exists. Will not overwrite.\n")
        return False
    elif not is_directory_writable(os.path.dirname(mutables['outfile'])):
        sys.stderr.write(f"Error: Cannot write to Output file [{mutables['outfile']}].\n")
        return False

    if os.path.exists(mutables['keyfile']):
        if os.access(mutables['keyfile'], os.R_OK):
            sys.stdout.write(f"Using existing Key file [{mutables['keyfile']}].\n")
        else:
            sys.stderr.write(f"Error: Cannot open Key file [{mutables['keyfile']}].\n")
            return False
    elif not is_directory_writable(os.path.dirname(mutables['keyfile'])):
        sys.stderr.write(f"Error: Cannot write to Key file [{mutables['keyfile']}].\n")
        return False
    
    return True

def decryption_preparation(infile, mutables, ext):
    if not os.access(infile, os.F_OK & os.R_OK):
        sys.stderr.write(f"Error: Cannot open Input file [{infile}].\n")
        return False

    if not mutables['outfile']:
        if infile.endswith(enc_ext):
            mutables['outfile'] = infile[: -len(enc_ext)]
        else:
            mutables['outfile'] = infile + dec_ext
        sys.stdout.write(f"Assuming Output file [{mutables['outfile']}].\n")
    if not mutables['keyfile']:
        if infile.endswith(enc_ext):
            mutables['keyfile'] = infile[: -len(enc_ext)] + ext
        else:
            mutables['keyfile'] = infile + ext
        sys.stdout.write(f"Assuming Key file [{mutables['keyfile']}].\n")

    if os.path.exists(mutables['outfile']):
        sys.stderr.write(f"Error: Output file [{mutables['outfile']}] already exists. Will not overwrite.\n")
        return False
    elif not is_directory_writable(os.path.dirname(mutables['outfile'])):
        sys.stderr.write(f"Error: Cannot write to Output file [{mutables['outfile']}].\n")
        return False

    if not os.access(mutables['keyfile'], os.F_OK & os.R_OK):
        sys.stderr.write(f"Error: Cannot open Key file [{mutables['keyfile']}].\n")
        return False
    
    return True

def encrypt_with_key(infile, keyfile, outfile):
    mutables = {'outfile':outfile, 'keyfile':keyfile}
    if not encryption_preparation(infile, mutables, key_ext):
        return

    import my_py_crypt_lib
    if not os.path.exists(mutables['keyfile']):
        sys.stdout.write(f"Creating Key file [{mutables['keyfile']}].\n")
        my_py_crypt_lib.create_key(mutables['keyfile'])

    key = my_py_crypt_lib.load_key(mutables['keyfile'])
    my_py_crypt_lib.encrypt(infile, key, mutables['outfile'])

def decrypt_with_key(infile, keyfile, outfile):
    mutables = {'outfile':outfile, 'keyfile':keyfile}
    if not decryption_preparation(infile, mutables, key_ext):
        return

    import my_py_crypt_lib
    key = my_py_crypt_lib.load_key(mutables['keyfile'])
    my_py_crypt_lib.decrypt(infile, key, mutables['outfile'])

def encrypt_with_sap(infile, keyfile, outfile):
    mutables = {'outfile':outfile, 'keyfile':keyfile}
    if not encryption_preparation(infile, mutables, salt_ext):
        return

    import getpass
    password1 = getpass.getpass("Enter Password: ")
    password2 = getpass.getpass("Re-enter Password: ")
    if password1 != password2:
        sys.stderr.write("Error: Entered passwords don't match.\n")
        return

    import my_py_crypt_lib
    if not os.path.exists(mutables['keyfile']):
        sys.stdout.write(f"Creating Key file [{mutables['keyfile']}].\n")
        my_py_crypt_lib.create_salt(mutables['keyfile'])

    salt = my_py_crypt_lib.load_salt(mutables['keyfile'])
    key = my_py_crypt_lib.generate_key(salt, password1)
    my_py_crypt_lib.encrypt(infile, key, mutables['outfile'])

def decrypt_with_sap(infile, keyfile, outfile):
    mutables = {'outfile':outfile, 'keyfile':keyfile}
    if not decryption_preparation(infile, mutables, salt_ext):
        return

    import getpass
    password = getpass.getpass("Enter Password: ")

    import my_py_crypt_lib
    salt = my_py_crypt_lib.load_salt(mutables['keyfile'])
    key = my_py_crypt_lib.generate_key(salt, password)
    my_py_crypt_lib.decrypt(infile, key, mutables['outfile'])
