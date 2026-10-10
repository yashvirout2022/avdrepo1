import os 

print("Jenkins Credential")

username = os.getenv('username')
password = os.getenv('password')

print('Username', username)
print('Password', password)


