import random
import time
import matplotlib.pyplot as plt


def timer(sequence):
    start = time.time()
    max_subsequence3(sequence)
    end = time.time()
    return end - start


def max_subsequence3(s):
    maxSum = 0                  # O(1)
    testSum = 0                 # O(1)
    for i in range(len(s)):     # O(n)
        testSum += s[i]         # O(1)
        if testSum > maxSum:    # O(1)
            maxSum = testSum    # O(1)
        if testSum < 0:         # O(1)
            testSum = 0         # O(1)
    return maxSum               # O(1)


random.seed(17)
sampleList = list(range(-500, 501))*1000
list1 = random.sample(sampleList, 62500)
list2 = random.sample(sampleList, 125000)
list3 = random.sample(sampleList, 250000)
list4 = random.sample(sampleList, 500000)
list5 = random.sample(sampleList, 1000000)

a = timer(list1)
b = timer(list2)
c = timer(list3)
d = timer(list4)
e = timer(list5)

x = [62500, 125000, 250000, 500000, 1000000]
y = [a, b, c, d, e]

print(a,b,c,d,e)
print(b/a)
print(c/b)
print(d/c)
print(e/d)

plt.figure()
plt.xlabel('Length of input sequence [n]')
plt.ylabel('Seconds [s]')
plt.title("Time complexity for 'max_subsequence3'")
plt.plot(x, y)
plt.show()

# When doubling the input, the time to compute takes roughly doubles which gives O(n)
