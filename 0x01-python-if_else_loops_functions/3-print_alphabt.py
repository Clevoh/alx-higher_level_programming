#ascii_value of 'a' and 'z'
start = ord('a')
end = ord('z')

for ascii_value in range(start, end + 1):
    if chr(ascii_value) not in ('q', 'e'):
        print(chr(ascii_value), end='')

print()
