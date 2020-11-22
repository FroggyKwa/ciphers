#  Ciphers's cipher


def rotate(string, n):
    result = str()
    for elm in string:
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
rot = int(input('Enter rotate_n: '))
ok = False
while not ok:
    if 0 > rot or rot > limit:
        rot = int(input(f'Rotate value is incorrect. Choose value from [0 to {limit - 1}]'))
    else:
        ok = True

print(f'Result is: {rotate(s, rot)}')
