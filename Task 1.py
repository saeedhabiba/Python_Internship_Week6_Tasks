import math
import statistics

numbers = [4, 9, 16, 25]

#square roots
square_roots = [math.sqrt(n) for n in numbers]
print("Square roots:", square_roots)

#average
average = statistics.mean(numbers)
print("Average:", average)