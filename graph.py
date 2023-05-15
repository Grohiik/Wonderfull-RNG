import matplotlib.pyplot as plt
import math
import numpy as np


numbers = []
            # numbers.append(1.0/(float(number)/5000000.0))


with open('numbers.txt','r') as f:
    file = f.readlines()
    for row in file:
        row = int(row[:-1])
        # numbers.append(row)
        i = 0b1000000000000000
        while(i):
            number = row&i
            i = i >> 1

            if number:
                numbers.append((int(math.log2(number))+1))


# numbers = numbers[:-1]

labels, counts = np.unique(numbers, return_counts=True)
labels = np.insert(labels[:-8], 1, labels[-8:])
counts = np.insert(counts[:-8], 1, counts[-8:])
counts = [number/len(file)*100 for number in counts]


plt.bar(labels, counts)
plt.ylabel("Procent")
plt.xlabel("bit position")

# Get your current y-ticks (loc is an array of your current y-tick elements)
# loc, labels = plt.yticks()

# This sets your y-ticks to the specified range at whole number intervals
# plt.yticks(np.arange(0, max(loc), step=1))
plt.show()