class User:

    def __init__(self, id, username):
        self.id = id
        self.username = username
        self.follower = 0

user = User("001", input("What is your name: "))
name = user.username
follower = user.follower
follower += 100
print(f"hello {name}, you have {follower} followers")