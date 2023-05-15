import serial
import hashlib
from bitarray import bitarray

serialPort = serial.Serial(
    port="COM8", baudrate=115200, bytesize=8
)

mybits = bitarray(endian='little')
mybytes = bytearray()
serialString = ""  # Used to hold data coming over UART
while 1:
    # Wait until there is data waiting in the serial buffer
    if serialPort.in_waiting > 0:

        # Read data out of the buffer until a carraige return / new line is found
        serialString = serialPort.readline()

        # Print the contents of the serial data
        try:
            number = int(serialString.decode("Ascii")[:-1])
             
            #SHA256 sliding window
            mybytes.extend((number&255).to_bytes(1, 'little', signed=False))
            if len(mybytes) >= 32:
                with open("sliding_window_second_iteration.bin", "a+b") as f:
                    sha = hashlib.sha256(mybytes).digest()
                    f.write(sha)
                    print(sha.hex())
                    mybytes = mybytes[-31:]


            # print(number)
        except:
            pass
