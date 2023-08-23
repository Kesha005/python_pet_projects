from cryptography.fernet import Fernet

message = "hello Kerim"

key = Fernet.generate_key()

fernet = Fernet(key)

enc_message = fernet.encrypt(message.encode())
print(f'Orginal string {message} \n')
print(f'Encrypted data {enc_message}')


decr_msg= fernet.decrypt(enc_message.decode())

print(decr_msg.decode())