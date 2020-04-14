import random
import math
import matplotlib.pyplot as plt

# Initialization
total = 450 # Number of Dart
hit = 0 # Number of dart fall inside the circle's part
ndart = 0 # Number of threw dart

# Throw Dart
for dart in range(0,total):
    Xrand = random.randint(0,1)
    Yrand = random.randint(0,1)
    ndart += 1
    # Check Condition
    if (Xrand**2)+(Yrand**2)<=1:
        hit += 1

print("Total Dart = "+str(total))
print("Hits = "+str(hit))
print("Throws = "+str(ndart)+" times")
pi = (hit/total)*4
print("Pi = "+str(pi))
errorDecimal = math.pi-pi
percent = (pi/math.pi)*100
errorPercent = 100-percent
print("Error = "+str(errorPercent)+"%")
