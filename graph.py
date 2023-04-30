import matplotlib.pyplot as plt
import math


numbers = []
            # numbers.append(1.0/(float(number)/5000000.0))


with open('mod50.txt','r') as f:
    for row in f:
        row = int(row[:-1])
        numbers.append(row)
        # i = 0b10000000
        # while(i):
        #     number = row&i
        #     i = i >> 1

        #     if number:
        #         numbers.append(int(math.log2(number))+1)
                


numbers = numbers[:-1]

plt.hist(numbers, bins=50)
plt.show()