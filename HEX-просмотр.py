import math


def my_hex(n):
    q = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
    new_n = ''
    while n:
        new_n += q[n % 16]
        n //= 16
    return new_n[::-1]


with open('data.txt', 'rb') as f:
    bin_text = f.read()


bin_lst, lst = [], []

for i in range(math.ceil(len(bin_text) / 16)):
    bin_lst.append(bin_text[16 * i if i else 0: 16 * (i + 1)])
    lst.append(''.join(chr(i) if chr(i).isprintable() else '.' for i in bin_text[16 * i if i else 0: 16 * (i + 1)]))

print('          00 01 02 03 04 05 06 07 08 09 0a 0b 0c 0d 0e 0f  \n')
for i in range(len(lst)):
    s = ((hex(i * 16)[hex(i * 16).index('x') + 1:].rjust(6, '0') + '    ' +
          ' '.join(hex(k)[hex(k).index('x') + 1:].rjust(2, '0') for k in bin_lst[i])).
         ljust(62, ' ') + lst[i])
    print(s.replace('\n', ''))

