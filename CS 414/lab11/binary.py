bits = []
def bits_to_int(bits):
    total = 0
    pow2  = 1
    for bit in bits:
        total += bit * pow2
        pow2 *= 2
    return total

def int_to_bits(num):
    if num == 0:
        return [0]
    else:
        bits = []
        while num > 0:
            last_bit = num % 2
            bits.append(last_bit )
            num = num // 2
        return bits

def digits_to_int(digits, base):
    total = 0
    pow2  = 1
    for digit in digits:
        total += digit * pow2
        pow2 *= base
    return total

def int_to_digits(num, base):
    if num == 0:
        return [0]
    else:
        digits = []
        while num > 0:
            last_digit = num % base
            digits.append(last_digit)
            num = num // base
        return digits


def bit_string_to_int(bit_string):
    list(bit_string)
    bit_strings = str(bit_string)
    bits = []
    reversed_bits = []
    for bit_string in bit_strings:
        bit_new = int(bit_string)
        bits.append(bit_new)
    bits.reverse()
    return bits_to_int(bits)

def main():
    print ('int_to_bits(25) =', int_to_bits(25))
    print ('int(11001) =', bits_to_int([1,0,0,1,1]))
    print ('digits_to_int([1,2,3,0], 10) =', digits_to_int([1,2,3,0], 10))
    print ('int_to_digits(1230, 10) =',      int_to_digits(1230, 10))
    print ("bit_string_to_int('11011') =",   bit_string_to_int('11011'))

if __name__ == '__main__':
    main()

#RS
