from cryptography.fernet import Fernet

key = Fernet.generate_key()

fernet = Fernet(key)


with open("file_key.key","wb") as filekey:
    filekey.write(key)

with open('some.txt','rb') as file:
    original = file.read()


encrypted = fernet.encrypt(original)

with open('some.txt','wb') as enc_file:
    enc_file.write(encrypted)