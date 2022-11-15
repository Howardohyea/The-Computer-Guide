import time

pi = 0
accuracy =int(input("input accuracy"))
#one billion is 1000000000

startTime = time.time()

for i in range(0, accuracy):
    pi += ((4.0 * (-1)**i) / (2*i + 1))

print("%.15f" % p)

executionTime = (time.time() - startTime)
print('Execution time in seconds: ' + str(executionTime))
