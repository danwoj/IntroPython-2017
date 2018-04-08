import nacl.pwhash
password = b'my password'

for i in range(4):
    print(nacl.pwhash.str(password))
# if needed, each hasher is exposed
# in just the same way:
for i in range(4):
    print(nacl.pwhash.scrypt.str(password))

for i in range(4):
     print(nacl.pwhash.argon2i.str(password))

# and

for i in range(4):
     print(nacl.pwhash.argon2id.str(password))