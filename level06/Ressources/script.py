lengh = 10
string = "alan le plus beau"

v4 = (ord(string[3]) ^ 4919) + 6221293
for i in range (0, len(string)):
    if (ord(string[i]) <= 31):
        exit()
    v4 += (v4 ^ ord(string[i])) % 1337
print(v4)
