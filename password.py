'''Write a function named is_valid that gets two strings arguments, username and password.
The function will return True if the username and password are valid in the system, otherwise False.
Our system contains only two valid usernames - "admin" and "user".
The valid password for username "user" is "qweasd".
For username "admin" any password is valid!'''

def is_valid(username, password):
    if (username == 'user' and password == 'qweasd') or username == 'admin':
        return True
    else:
        return False
    
user_username = input()
user_password = input()
print(is_valid(user_username, user_password))