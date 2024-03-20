encrypted_string = "Q}|u`sfg~sf{}|a3"
decrypted_string = "Congratulations!"

a1_value = ""
val = 0
for i in range(len(encrypted_string)):
    decrypted_char = decrypted_string[i]
    encrypted_char = encrypted_string[i]
    print((ord(encrypted_char) ^ ord(decrypted_char)))

print("The value of a1 is:", a1_value)