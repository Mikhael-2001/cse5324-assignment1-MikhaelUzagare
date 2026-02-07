import hashlib

class UserAuth:
    def __init__(self):
        self.users = {}

    def register(self, username, password):
        if username in self.users: return False
        hashed = hashlib.sha256(password.encode()).hexdigest()
        self.users[username] = hashed
        return True

    def login(self, username, password):
        if username not in self.users: return False
        hashed = hashlib.sha256(password.encode()).hexdigest()
        return self.users[username] == hashed

if __name__ == "__main__":
    auth = UserAuth()
    auth.register("alice", "password123")
    print(f"Login success: {auth.login('alice', 'password123')}")