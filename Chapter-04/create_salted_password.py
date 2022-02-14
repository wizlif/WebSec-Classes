import hashlib
import hashlib
import uuid

password = 'XXXXXX' # Replace with your own password

salt = uuid.uuid4() # Generate UUID 4 salt

salted_password = f'{salt}{password}' # Combine password with salt

final_hash = hashlib.md5(salted_password.encode()).hexdigest()

# STore salt & final hash
print('##### SALT #####\n')
print(salt)

print('\n\n##### HASH #####\n')
print(final_hash)
