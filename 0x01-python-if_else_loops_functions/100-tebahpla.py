#!/usr/bin/python3

def print_reverse_alphabet():
    for ascii_value in range(ord('z'), ord('a') - 1, -1):
        if (ascii_value - ord('z')) % 2 == 0:
            print(chr(ascii_value), end='')
        else:
            print(chr(ascii_value).upper(), end='')

print_reverse_alphabet()

