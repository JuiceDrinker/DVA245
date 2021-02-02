import random
import time
import matplotlib.pyplot as plt


def timer(sequence):
    start = time.time()
    max_subsequence1(sequence)
    end = time.time()
    return end - start


def max_subsequence1(s):
    maxSum = 0                          # O(1)
    for i in range(len(s)):             # O(n)
        for j in range(i, len(s)):      # O(n^2)
            testSum = 0                 # O(1)
            for k in range(i, j+1):     # O(n^3)
                testSum += s[k]         # O(1)
            if testSum > maxSum:        # O(1)
                maxSum = testSum        # O(1)
    return maxSum                       # O(1)


random.seed(17)
sampleList = list(range(-500, 501))*1000
list1 = random.sample(sampleList, 80)
list2 = random.sample(sampleList, 160)
list3 = random.sample(sampleList, 320)
list4 = random.sample(sampleList, 640)
list5 = random.sample(sampleList, 1280)

a = timer(list1)
b = timer(list2)
c = timer(list3)
d = timer(list4)
e = timer(list5)

x = [80, 160, 320, 640, 1280]
y = [a, b, c, d, e]
print(a,b,c,d,e)
print(b/a)
print(c/b)
print(d/c)
print(e/d)

plt.figure()
plt.xlabel('Length of input sequence [n]')
plt.ylabel('Seconds [s]')
plt.title("Time complexity for 'max_subsequence1'")
plt.plot(x, y)
plt.show()

# When doubling the input, the time to compute takes roughly 8 times longer which gives O(n^3)
