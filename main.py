class User:
    def __init__(self, Id,Name):
        self.id = Id
        self.name = Name
        self.followers = 0
        self.following = 0
    def follow(self, user):
        user.followers += 1
        self.following += 1 





user_1 = User('001','Bilal')
user_2 = User('002','Alveena')

user_1.follow(user_2)

print('User 1 ID',user_1.id)
print('User 1 Name',user_1.name)
print('User 1 Follower', user_1.followers)
print('User 1 following',user_1.following)
print('User 2 ID',user_2.id)
print('User 2 Name',user_2.name)
print('User 2 Follwers', user_2.followers)
print('User 2 Following', user_2.following)