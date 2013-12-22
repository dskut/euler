#! /usr/bin/env python

import sys
import os
import math
import string

def str_to_codes(s):
    return [ord(x) for x in s]

def codes_to_str(codes):
    return ''.join([chr(c) for c in codes])

def decrypt(msg_codes, key_codes):
    size = len(msg_codes)
    key_size = len(key_codes)
    res_codes = []
    is_valid = True
    for i in xrange(0, size):
        msg_code = msg_codes[i]
        key_code = key_codes[i % key_size]
        res_code = msg_code ^ key_code
        symbol = chr(res_code)
        if res_code < 32 or symbol in '~+=<>`':
            is_valid = False
            break
        res_codes.append(res_code)
    return is_valid, codes_to_str(res_codes), res_codes

def main():
    if len(sys.argv) < 2:
        print "usage: " + sys.argv[0] + " <cipher1.txt>"
        exit(1)

    cipher_path = sys.argv[1]
    cipher_file = open(cipher_path)
    codes = []
    for line in cipher_file:
        str_codes = line.strip().split(',')
        codes += [int(code) for code in str_codes]
    cipher_file.close()

    alphabet = string.ascii_lowercase + '0123456789!#$%&()*-+,:;=?.'

    for a in alphabet:
        for b in alphabet:
            for c in alphabet:
                key = a + b + c
                key_codes = str_to_codes(key)
                is_valid, message, msg_codes = decrypt(codes, key_codes)
                #print "codes:", codes
                #print "key:", key
                #print "key codes:", key_codes
                #print "msg_codes:", msg_codes
                #print "message:", message
                #print message
                if is_valid:
                    print key
                    print message
                    print sum(msg_codes)
                    #return 0
                #else:
                    #print "nope"

main()
