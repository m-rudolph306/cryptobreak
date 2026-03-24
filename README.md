# cryptobreak

Python toolkit demonstrating classical cryptographic attacks.

## Attacks implemented

| Attack | Description | File |
|---|---|---|
| CBC Bit-Flipping | Manipulate plaintext via ciphertext | attacks/cbc_bitflip.py |

## Usage

    python -m attacks.cbc_bitflip

## Write-ups

Each attack has a detailed write-up explaining the theory and implementation:
- [CBC Bit-Flipping](writeups/cbc_bitflip.md)

## Setup

    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    pytest
