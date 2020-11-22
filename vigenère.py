# Vigenère cipher


def rotate(s: str, k: str):
    result = str()
    for i, elm in enumerate(s):
        n = 0
        if k[i % len(k)].isalpha():
            n = ord(k[i % len(k)]) % 97
        if elm.isalpha():
            if elm.islower() and ord(elm) + n > 122:
                result += chr((ord(elm) + n) % 122 + 96)
            elif elm.isupper() and ord(elm) + n > 90:
                result += chr((ord(elm) + n) % 90 + 64)
            else:
                result += chr(ord(elm) + n)
        else:
            result += elm
    return result


limit = 26
s = input('Enter string to encode: ')
key = input('Enter key: ')
ok = False

print(f'Result is: {rotate(s, key)}')
