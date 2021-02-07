import random
import time
import matplotlib.pyplot as plt


def timer(sequence):
    start = time.time()
    max_subsequence2(sequence)
    end = time.time()
    return end - start


def max_subsequence2(s):
    maxSum = 0                      # O(1)
    for i in range(len(s)):         # O(n)
        testSum = 0                 # O(1)
        for j in range(i, len(s)):  # O(n^2)
            testSum += s[j]         # O(1)
            if testSum > maxSum:    # O(1)
                maxSum = testSum    # O(1)
    return maxSum                   # O(1)


random.seed(17)
sampleList = list(range(-500, 501))*1000
list1 = random.sample(sampleList, 500)
list2 = random.sample(sampleList, 1000)
list3 = random.sample(sampleList, 2000)
list4 = random.sample(sampleList, 4000)
list5 = random.sample(sampleList, 8000)

a = timer(list1)
b = timer(list2)
c = timer(list3)
d = timer(list4)
e = timer(list5)

x = [500, 1000, 2000, 4000, 8000]
y = [a, b, c, d, e]

print(a,b,c,d,e)
print(b/a)
print(c/b)
print(d/c)
print(e/d)

plt.figure()
plt.xlabel('Length of input sequence [n]')
plt.ylabel('Seconds [s]')
plt.title("Time complexity for 'max_subsequence2'")
plt.plot(x, y)
plt.show()

# When doubling the input, the time to compute takes roughly 4 times longer which gives O(n^2)
