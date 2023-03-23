# Importing the required modules
from cryptography.hazmat.primitives.asymmetric import rsa, padding

# Generating a public-private key pair
private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
public_key = private_key.public_key()

# Defining a message to be encrypted
message = b"Hello, world!"

# Encrypting the message using the public key
encrypted = public_key.encrypt(message, padding.OAEP(mgf=padding.MGF1(algorithm=padding.MGF1.ALGORITHM_SHA1), algorithm=padding.OAEPAlgorithm.ALGORITHM_SHA1, label=None))

# Decrypting the message using the private key
decrypted = private_key.decrypt(encrypted, padding.OAEP(mgf=padding.MGF1(algorithm=padding.MGF1.ALGORITHM_SHA1), algorithm=padding.OAEPAlgorithm.ALGORITHM_SHA1, label=None))

# Printing the original message and the decrypted message
print(f"Original message: {message.decode()}")
print(f"Decrypted message: {decrypted.decode()}")