key = [[6, 24, 1],
       [13, 16, 10],
       [20, 17, 15]]


def hill_encrypt(plaintext):
    ciphertext = ""

    if len(plaintext) % 3 == 2:
        plaintext += "Z"
    elif len(plaintext) % 3 == 1:
        plaintext += "ZZ"

    for i in range(len(plaintext) // 3):
        for j in range(3):
            temp = 0
            for k in range(3):
                p = ord(plaintext[i*3+k])-65
                c = p * key[j][k]
                temp += c
            ciphertext += chr(temp % 26 + 65)

    return ciphertext


def hill_decrypt(ciphertext):
    plaintext = ""
    arr = []
    k_inv = [[0] * 3 for i in range(3)]

    det = key[0][0]*key[1][1]*key[2][2] + key[0][1] * \
        key[1][2]*key[2][0] + key[0][2]*key[1][0]*key[2][1]
    det = det - key[2][0]*key[1][1]*key[0][2] - key[2][1] * \
        key[1][2]*key[0][0] - key[2][2]*key[1][0]*key[0][1]
    det %= 26

    for i in range(3):
        for j in range(3):
            arr.clear()
            for k in range(3):
                if k != i:
                    for l in range(3):
                        if l != j:
                            arr.append(key[k][l])
            k_inv[j][i] = ((arr[0]*arr[3] - arr[1]*arr[2]))
            if (j+i) % 2 == 1:
                k_inv[j][i] *= -1
            k_inv[j][i] = (k_inv[j][i]*25) % 26

    for i in range(len(ciphertext) // 3):
        for j in range(3):
            temp = 0
            for k in range(3):
                c = ord(ciphertext[i*3+k])-65
                p = int(c * k_inv[j][k])
                temp += p
            plaintext += chr(temp % 26 + 65)

    return plaintext


print(hill_encrypt("ILKOMPUGM"))
print(hill_decrypt("KQDXEHQIG"))
