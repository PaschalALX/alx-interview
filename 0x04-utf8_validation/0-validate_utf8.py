#!/usr/bin/python3

""" Determines if a given data set represents a valid UTF-8 encoding """


def reverse_bits(num):
    """ reverses bits and returns list of bits """

    bits = []

    while num:
        bit = num & 1
        bits.append(bit)
        num >>= 1

    bits.reverse()
    return bits


def isASCII(num):
    """ checks if number is ASCII encoded """

    if num < 128:
        return True

    return False


def isUTF8(num):
    """ checks if number is UTF8 encoded """

    if isASCII(num):
        return True

    bits = reverse_bits(num)
    header_bit_cnt = 0

    while header_bit_cnt < (len(bits) - 1):
        if not bits[header_bit_cnt]:
            break
        header_bit_cnt += 1

    if len(bits) != header_bit_cnt * 8:
        return False

    contag_bit_idx = 8
    while contag_bit_idx < len(bits):
        if not bits[contag_bit_idx] == 1 and bits[contag_bit_idx + 1] == 0:
            return False
        contag_bit_idx += 8

    return True


def validUTF8(data):
    """ determines if a given data set represents a valid UTF-8 encoding """

    if not data or type(data) != list:
        return False

    if not len(data):
        return True

    for x in data:
        if not isUTF8(x):
            return False

    return True
