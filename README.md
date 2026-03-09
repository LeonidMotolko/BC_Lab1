# AES-128 Decryption & ECC Digital Signature 

Simple cryptography project written in **Python** demonstrating:

-   SHA-256 key verification
-   AES-128 decryption (CBC mode)
-   Elliptic Curve key generation
-   ECDSA digital signature

------------------------------------------------------------------------

# Result

  Item                  Value
  --------------------- ------------------------------------
  Correct AES Key       `54684020247570407220244063724074`
  Decrypted Message     `Hello Blockchain!`
  Curve                 `P-256`
  Signature Algorithm   `ECDSA`

------------------------------------------------------------------------

# Input Data

## Candidate AES Keys

    68544020247570407220244063724074
    54684020247570407220244063724074
    54684020247570407220244063727440

## Expected SHA-256 Hash

    f28fe539655fd6f7275a09b7c3508a3f81573fc42827ce34ddf1ec8d5c2421c3

## AES Ciphertext

    876b4e970c3516f333bcf5f16d546a87aaeea5588ead29d213557efc1903997e

## Initialization Vector

    656e6372797074696f6e496e74566563

------------------------------------------------------------------------

# How It Works

## 1. Key Identification

Each candidate key is processed as:

    HEX → bytes → SHA-256

Then the hash is compared to the expected value:

    if sha256(key) == expected_hash

The matching key becomes the **correct AES key**.

------------------------------------------------------------------------

## 2. AES Decryption

Configuration:

    Algorithm : AES-128
    Mode      : CBC
    IV        : 656e6372797074696f6e496e74566563

Steps:

1.  Convert ciphertext from HEX to bytes\
2.  Initialize AES cipher\
3.  Decrypt ciphertext\
4.  Remove PKCS#7 padding

Result:

    Hello Blockchain!

------------------------------------------------------------------------

## 3. ECC Key Generation

An asymmetric key pair is generated using:

    Curve: P-256

This produces:

-   Private key
-   Public key

The public key is exported in **PEM format**.

------------------------------------------------------------------------

## 4. Digital Signature

The decrypted message is signed using **ECDSA**.

Process:

    plaintext → SHA256 → sign(private_key)

Output:

    ECDSA signature (HEX)

------------------------------------------------------------------------

# Project Structure

    crypto-assignment
    │
    ├── main.py
    └── README.md

------------------------------------------------------------------------

# Installation

``` bash
pip install pycryptodome
```

------------------------------------------------------------------------

# Run

``` bash
python main.py
```

------------------------------------------------------------------------

# Example Output

    Correct key:
    54684020247570407220244063724074

    Decrypted message:
    Hello Blockchain!

    Public key:
    -----BEGIN PUBLIC KEY-----
    ...
    -----END PUBLIC KEY-----

    Signature:
    3045022100...

------------------------------------------------------------------------

# Technologies

  Tool           Purpose
  -------------- -------------------------
  Python         Implementation
  PyCryptodome   Cryptographic library
  AES            Symmetric encryption
  ECC            Asymmetric cryptography
  ECDSA          Digital signatures

------------------------------------------------------------------------

# Author

**Leanid Matolka**
