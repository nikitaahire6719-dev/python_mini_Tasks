import string

class PasswordValidator:
    def validate(self, password):
        rules = {"length": len(password) >= 8, 
                 "lowercase": any(c in string.ascii_lowercase for c in password), 
                 "uppercase": any(c in string.ascii_uppercase for c in password), 
                 "digit": any(c in string.digits for c in password), 
                 "special": any(c in string.punctuation for c in password)}
        return rules
    def is_strong(self, password):
        rules = self.validate(password)
        return all(rules.values())