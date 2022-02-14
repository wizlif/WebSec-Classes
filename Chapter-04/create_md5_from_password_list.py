import hashlib

# Open password file
password_file = open('passwords.txt','r')

# Read all the passwords to a list
passwords = password_file.readlines()

# hash passwords
md5_file = open('md5_passwords.txt','w')

md5_file.writelines([passwords[index][:-1]+' -> '+hashlib.md5(password.encode()).hexdigest()+'\n' for index,password in enumerate(passwords)])
