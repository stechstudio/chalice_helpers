import os
import boto3
import base64
from typing import Any, Optional


def env(key, default=''):
    """Retrieve a key from the environment
    :param key: A key name that is expected to exist.
    :param default: A default if the key does not exist.
    :return: string
    """
    # type: (str, Optional[Any]) -> str
    if key.endswith('_SECRET'):
        return env_secret(key, default)

    return os.environ.get(key, default)


def env_secret(key, default=''):
    """Retrieve a secret key from the environment, decrypt it and return the plaintext
    :param default: What to use if the key does not exist
    :param key: A key name that is expected to exist.
    :return: string
    """
    # type: (str, Optional[Any]) -> str
    encoded = os.environ.get(key)

    if encoded is None and default == '':
        return default

    if encoded is None:
        encoded = default

    return decrypt(encoded)


def encrypt(key_id, plaintext):
    """Given an AWS KMS Key ID and a string, encrypt the string with the key."""
    # type: (str, str) -> str
    binary_encrypted = boto3.client('kms').encrypt(KeyId=key_id, Plaintext=plaintext)['CiphertextBlob']
    encoded = base64.b64encode(binary_encrypted)
    return encoded.decode()


def decrypt(encoded):
    """Given an encoded string, decrypt it with a KMS Key."""
    # type: str -> str
    binary_encrypted = base64.b64decode(encoded)
    decrypted = boto3.client('kms').decrypt(CiphertextBlob=binary_encrypted)['Plaintext']
    return decrypted.decode()
