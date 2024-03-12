#!/usr/bin/python3

def print_reverse_alphabet():
    for ascii_value in range(ord('z'), ord('a') - 1, -1):
        print("{:c}".format(ascii_value - (ord('a') - ord('A')) * ((ascii_value - ord('z')) % 2)), end=' ')

print_reverse_alphabet()

