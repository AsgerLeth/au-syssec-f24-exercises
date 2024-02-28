import random
from Crypto.Cipher import AES
import time
import datetime

# Convert the date to a Unix timestamp
start_date = datetime.datetime(2024, 2, 19, 0, 0)
end_date = datetime.datetime(2024, 2, 20, 0, 0)
start_timestamp = int(start_date.timestamp())
end_timestamp = int(end_date.timestamp())

def attempt_decrypt(encrypted_file_path, decrypted_file_path, potential_key):
    try:
        with open(encrypted_file_path, 'rb') as f_encrypted:
            nonce = f_encrypted.read(16)  # Read the nonce
            tag = f_encrypted.read(16)    # Read the tag
            ciphertext = f_encrypted.read()  # Read the remaining ciphertext

        # Initialize AES GCM with the potential key and nonce
        aes = AES.new(potential_key, AES.MODE_GCM, nonce=nonce)
        # Attempt to decrypt and verify the ciphertext
        data = aes.decrypt_and_verify(ciphertext, tag)

        # If successful, write the decrypted data to a file
        with open(decrypted_file_path, 'wb') as f_decrypted:
            f_decrypted.write(data)
        
        return True  # Decryption was successful
    except Exception as e:
        return False  # Decryption failed

for timestamp in range(start_timestamp, end_timestamp):
    random.seed(timestamp)
    potential_key = random.randbytes(16)
    if attempt_decrypt("ciphertext.bin", "decrypted.txt", potential_key):
        print(f"Decryption successful with timestamp: {timestamp}")
        break
