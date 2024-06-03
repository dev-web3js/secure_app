from cryptography.fernet import Fernet  # Import Fernet for symmetric encryption

# Generate a key for encryption and decryption
key = Fernet.generate_key()  # Generate a new key for encryption
cipher_suite = Fernet(key)  # Create a Fernet cipher suite using the generated key

def encrypt_data(data):
    """Encrypt data using Fernet symmetric encryption."""
    if isinstance(data, str):  # Check if the data is a string
        data = data.encode('utf-8')  # Encode the string data to bytes
    return cipher_suite.encrypt(data).decode('utf-8')  # Encrypt the data and decode it to a string

def decrypt_data(data):
    """Decrypt data using Fernet symmetric encryption."""
    return cipher_suite.decrypt(data.encode('utf-8')).decode('utf-8')  # Decrypt the data and decode it to a string
