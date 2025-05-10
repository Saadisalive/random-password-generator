import random
import string
import secrets

letters = string.ascii_letters

digits = string.digits

special_charts = string.punctuation

selection_list = letters + digits + special_charts

password_len = 10

password = ""
for i in range(password_len):
    password+=''.join(secrets.choice(selection_list))

print(password)