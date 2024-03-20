string = input()

s_encoded = (ord(string[3]) ^ 4919) + 6221293
for i in range(len(string)):
	s_encoded += (s_encoded ^ ord(string[i])) % 1337
print(s_encoded)