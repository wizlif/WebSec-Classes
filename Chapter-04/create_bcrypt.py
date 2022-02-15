import bcrypt
import time

password = b'Washere@93'

# $2b$17$ysOM4Y15j8NK1Nots9QOp.TuGTAIIJ2SRqAN7RfWVwp1di/4kk43q

start = time.time()
cost_factor = 17
salt = bcrypt.gensalt(rounds=cost_factor)
hash = bcrypt.hashpw(password, salt)
end = time.time()
print(end-start)
print(salt)
print(hash.decode())

# Sign In
sign_in_password = b'Washere@93'
if bcrypt.checkpw(sign_in_password, hash):
    print('Sign In successful')
else:
    print('Invalid Username or Password')

# Sign Up
# email = ''
# password = ''

# cost_factor = 17
# salt = bcrypt.gensalt(rounds=cost_factor)
# hash = bcrypt.hashpw(password, salt)

# 'INSERT INTO users (email,hash)'
