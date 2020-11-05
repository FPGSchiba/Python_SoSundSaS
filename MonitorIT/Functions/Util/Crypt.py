# Version 1.0
# Author: Jann Erhardt
# Build: 1.0

from Crypto.Cipher import AES
from Crypto.Util.Padding import *
from Crypto.Random import *


def writeKey(file):
    key = get_random_bytes(32)  # 32 bytes * 8 = 256 bits (1 byte = 8 bits)
    # Save the key to a file
    file_out = open(file, "wb")  # wb = write bytes
    file_out.write(key)
    file_out.close()


def readKey(file):
    # Later on ... (assume we no longer have the key)
    file_in = open(file, "rb")  # Read bytes
    key_from_file = file_in.read()  # This key should be the same
    file_in.close()
    return key_from_file


def encryptData(data, file, key):
    # Create cipher object and encrypt the data
    cipher = AES.new(key, AES.MODE_CBC)  # Create a AES cipher object with the key using the mode CBC
    ciphered_data = cipher.encrypt(pad(data, AES.block_size))  # Pad the input data and then encrypt

    file_out = open(file, "wb")  # Open file to write bytes
    file_out.write(cipher.iv)  # Write the iv to the output file (will be required for decryption)
    file_out.write(ciphered_data)  # Write the varying length ciphertext to the file (this is the encrypted data)
    file_out.close()


def readData(file, key):
    # Read the data from the file
    file_in = open(file, 'rb')  # Open the file to read bytes
    iv = file_in.read(16)  # Read the iv out - this is 16 bytes long
    ciphered_data = file_in.read()  # Read the rest of the data
    file_in.close()

    cipher = AES.new(key, AES.MODE_CBC, iv=iv)  # Setup cipher
    return unpad(cipher.decrypt(ciphered_data), AES.block_size)  # Decrypt and then up-pad the result
