## About

The Vigenère cipher is a method of encrypting alphabetic text using a simple form of polyalphabetic substitution. It uses a repeating keyword to shift letters in the alphabet, making it more secure than simple Caesar ciphers.

## How It Works

The Vigenère cipher works by:
1. Taking a plaintext message and a keyword
2. Repeating the keyword to match the length of the message
3. Shifting each letter in the message by the corresponding letter value in the key
4. For decryption, the process is reversed by shifting in the opposite direction

### Example
```
Message: "hello world"
Key:     "happycoding"
Result:  "oiwwc kvhwr"
```

## Usage

### Basic Example
```python
# Sample encrypted text and key
text = 'mrttaqrhknsw ih puggrur'
custom_key = 'happycoding'

# Decrypt the message
decryption = decrypt(text, custom_key)
print(f'Decrypted text: {decryption}')
```

### Encrypt Your Own Message
```python
# Encrypt a message
message = "your secret message"
key = "yourkey"
encrypted = encrypt(message, key)
print(f'Encrypted: {encrypted}')

# Decrypt it back
decrypted = decrypt(encrypted, key)
print(f'Decrypted: {decrypted}')
```

## Functions

### `vigenere(message, key, direction=1)`
Core function that handles both encryption and decryption.
- `message`: Text to encrypt/decrypt
- `key`: Keyword for the cipher
- `direction`: 1 for encryption, -1 for decryption

### `encrypt(message, key)`
Encrypts a message using the provided key.

### `decrypt(message, key)`
Decrypts a message using the provided key.


## Example Output

```
Encrypted text: mrttaqrhknsw ih puggrur
Key: happycoding

Decrypted text: vigenere is awesome
```
