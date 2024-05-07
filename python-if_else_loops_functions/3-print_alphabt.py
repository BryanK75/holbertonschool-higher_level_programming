#!/usr/bin/python3
i = ord('a')
alphabet = ''
while i <= ord('z'):
    if chr(i) != 'e' and chr(i) != 'q':
        alphabet += chr(i)
    i += 1

print(alphabet)
