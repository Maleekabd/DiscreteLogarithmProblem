#'latihan membuat cipher text menggunakan metode cipher text'

key = 'abcdefghijklmnopqrstuvwxyz'

print("==============================")
plaintext = input("plaintext : ")
key_subtitution = input("key : ")
print("==============================")

#keyToString = str(key_subtitution)
integer = int(key_subtitution)


def encript(integer, plaintext):
    result = ''
    for l in plaintext.lower():
        try:
            i = (key.index(l) + integer) % 26
            result += key[i]
            print(i)
        except ValueError:
            result += "1"
    return result.lower()


ciphertext = encript(integer, plaintext)
print("==============================")
print("cipher text : " + ciphertext)
print("==============================")

# decript


def decript(integer, ciphertext):
    result = ''
    for l in ciphertext.lower():
        i = (key.index(l) - integer) % 26
        result += key[i]
        print(i)
    return result.lower()


decriptsss = decript(integer, ciphertext)
print("==============================")
print("decript plaintext : " + decriptsss)
print("==============================")
