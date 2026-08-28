
def num_to_hex_str(number:bytes) -> str:
    filler_str = ''
    while number > 0:
        tmp = number >> 8 << 8
        tmp = number - tmp

        filler_str += '\\x' + tmp.to_bytes(byteorder='little').hex()
        number = number >> 8

    return filler_str

if __name__ == "__main__":
    hashcode = 0x21DD09EC
    filler = 0x01010101

    out_str = num_to_hex_str(filler)*4 + num_to_hex_str(hashcode - filler * 4)
    print('./col $(echo -ne \'' + out_str + '\')')


