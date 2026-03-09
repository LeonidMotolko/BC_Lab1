from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from Crypto.PublicKey import ECC
from Crypto.Signature import DSS
from Crypto.Hash import SHA256

# ----- 1. Finding the right key -----

keys = [
    "68544020247570407220244063724074",
    "54684020247570407220244063724074",
    "54684020247570407220244063727440"
]

target_hash = "f28fe539655fd6f7275a09b7c3508a3f81573fc42827ce34ddf1ec8d5c2421c3"

correct_key = None

for key_hex in keys:
    key_bytes = bytes.fromhex(key_hex)

    h = SHA256.new(key_bytes).hexdigest()

    if h == target_hash:
        correct_key = key_bytes
        print("Correct key:", key_hex)

# ----- 2. AES decryption -----

ciphertext = bytes.fromhex(
    "876b4e970c3516f333bcf5f16d546a87aaeea5588ead29d213557efc1903997e"
)

iv = bytes.fromhex(
    "656e6372797074696f6e496e74566563"
)

cipher = AES.new(correct_key, AES.MODE_CBC, iv)
plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)

print("Decrypted message:", plaintext.decode())

# ----- 3. Generating ECC keys -----

key = ECC.generate(curve='P-256')

private_key = key
public_key = key.public_key()

print("\nPublic key:")
print(public_key.export_key(format='PEM'))

# ----- 4. Creating a digital signature -----

hash_obj = SHA256.new(plaintext)
signer = DSS.new(private_key, 'fips-186-3')
signature = signer.sign(hash_obj)

print("Digital signature (HEX):")
print(signature.hex())