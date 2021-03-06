import pickle

from cryptography.fernet import Fernet


# @Version: 3.2
# @Author: Joshua Scina

class File_Manager:
    def __init__(self):
        # This key is only used for the default login
        self._master_key = self.gen_key()

    # Return the object
    def load(self, file):
        return pickle.load(file)

    # Dump the object
    def dump(self, obj, file):
        pickle.dump(obj, file)

    # Return master key

    def get_master(self):
        return self._master_key

    # Generate a new key
    def gen_key(self):
        key = Fernet.generate_key()
        return key

    # Create base files

    def gen_data(self):
        data = ([self.encrypt("Username", self.get_master())],
                [self.encrypt("Password", self.get_master())],
                [self.get_master()],
                [""],
                [""])
        with open("data.pp", "wb") as file:
            self.dump(data, file)
        del data

    # Dump data
    def dump_data(self, data: tuple):
        try:
            with open("data.pp", "wb") as file:
                self.dump(data, file)
            del data
        except FileNotFoundError:
            self.gen_data()

    # Load and return data
    def load_data(self):
        try:
            with open("data.pp", "rb") as file:
                data = self.load(file)
            return tuple(data)
        except FileNotFoundError:
            self.gen_data()
            return self.load_data()

    # Encrypt a string and return it
    def encrypt(self, phrase: str, key: bytes):
        crypto = Fernet(key)
        return crypto.encrypt(phrase.encode())

    # Decrypt bytes and return it as a string
    def decrypt(self, phrase: bytes, key: bytes):
        crypto = Fernet(key)
        return str(crypto.decrypt(phrase).decode())
