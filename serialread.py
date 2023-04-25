import serial
import hashlib

serialPort = serial.Serial(
    port="COM8", baudrate=115200, bytesize=8
)

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
                f.write(hashlib.sha256(number.to_bytes(16, 'little', signed=False)).digest())
            with open("random.bin", "a+b") as f:
                f.write(number.to_bytes(16, 'little', signed=False))
            print(serialString.decode("Ascii"), end="")
        except:
            pass