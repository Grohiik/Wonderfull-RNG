import serial
import hashlib
from bitarray import bitarray

serialPort = serial.Serial(
    port="COM8", baudrate=115200, bytesize=8
)

mybits = bitarray(endian='little')
serialString = ""  # Used to hold data coming over UART
while 1:
    # Wait until there is data waiting in the serial buffer
    if serialPort.in_waiting > 0:

        # Read data out of the buffer until a carraige return / new line is found
        serialString = serialPort.readline()

        # Print the contents of the serial data
        try:
            number = int(serialString.decode("Ascii")[:-1])

            with open("sha.bin", "a+b") as f:
                f.write(hashlib.sha256((number&255).to_bytes(1, 'little', signed=False)).digest())

            # bits = bitarray(endian='little')
            # bits.frombytes(number.to_bytes(16, 'little', signed=False))
            # after_extractor = bitarray()
            # while bits:
            #     bit1 = bits.pop()
            #     bit2 = bits.pop()

            #     if bit1 != bit2:
            #         after_extractor.append(bit1)
            # with open("von_neuman.bin", "a+b") as f:
            #     f.write(after_extractor)

            with open("numbers.txt", "+a") as f:
                f.write(serialString.decode("Ascii")[:-1])
            print(number)
        except:
            pass