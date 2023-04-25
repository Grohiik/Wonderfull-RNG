import matplotlib.pyplot as plt

numbers = []

with open('blub.txt','r') as f:
    for row in f:
        number = int(row[:-1])
        if number:
            numbers.append(1.0/(float(number)/5000000.0))


numbers = numbers[:-1]

plt.plot(numbers)
plt.ylabel('some numbers')
plt.show()