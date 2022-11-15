import time

pi = 0
accuracy =int(input("input accuracy"))
#A hundred million is 100000000, the recommended accuracy

startTime = time.time()

for i in range(0, accuracy):
    pi += ((4.0 * (-1)**i) / (2*i + 1))

print("%.15f" % pi)

executionTime = (time.time() - startTime)
print('Execution time in seconds: ' + str(executionTime))
