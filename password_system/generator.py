import secrets
import string

class PasswordGenerator:
    def generate(self, length=12):
        if length < 8:
            raise ValueError("Password length must be at least 8")
        
        chars = (string.ascii_lowercase + 
                 string.ascii_uppercase + 
                 string.digits + 
                 string.punctuation )

        password = "".join(secrets.choice(chars) for _ in range(length))
        return password