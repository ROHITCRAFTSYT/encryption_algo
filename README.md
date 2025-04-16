# Caesar Cipher

A simple Python implementation of the Caesar cipher encryption and decryption algorithm.

## Description

This program allows users to encrypt and decrypt text using the Caesar cipher technique. The Caesar cipher is one of the simplest and most widely known encryption techniques, where each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet.

## Features

- Encrypt any text using a customizable shift value
- Decrypt Caesar cipher encoded text when the shift value is known
- Preserves case (uppercase/lowercase)
- Maintains non-alphabetic characters (spaces, numbers, punctuation)
- Simple command-line interface

## Usage

Run the program:

```
python caesar_cipher.py
```

Follow the on-screen prompts to:
1. Choose between encryption and decryption
2. Enter the text to process
3. Specify the shift value (1-25)

## Examples

### Encryption
- Original: `Hello, World!`
- Shift: `3`
- Encrypted: `Khoor, Zruog!`

### Decryption
- Encrypted: `Khoor, Zruog!`
- Shift: `3`
- Decrypted: `Hello, World!`

## License

This project is open source and available under the [MIT License](LICENSE).
