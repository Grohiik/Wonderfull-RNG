from bitarray import bitarray

mybits = bitarray(endian='little')

with open("unProcessedNumbers.txt", "r") as f:
    
    for row in f:
        number = int(row[:-1])
        if number:
            byte = number.to_bytes(16, 'little', signed=False)
            mybits.frombytes(byte)

after = bitarray()
while mybits:
    bit1 = mybits.pop()
    bit2 = mybits.pop()

    if bit1 != bit2:
        after.append(bit1)

with open("von_neuman.bin", "wb") as f:
    f.write(after)
