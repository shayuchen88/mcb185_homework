import sys
import math

# copy of 32stats.py
number = []
for numbers in sys.argv[1:]:
    temp = float(numbers)
    number.append(temp)

number.sort()

print('The number of valuses is: ', number)
print("Total", len(number), "values in this sequence")

total = 0


for i in number:
    total += i

print("Sum: ", total)

print('Maximum value: ', max(number))
print('Minimum value: ', min(number))

mean = total/len(number)

print('The mean value is: ', mean)

sum_sqdiff = 0
for num in number:
    sqdiff = math.pow(num - mean, 2)
    sum_sqdiff += sqdiff

sd = math.sqrt(sum_sqdiff/len(number))
print('The sdandard deviation is: ', sd)

if len(number) % 2 != 0:
    print('The median is: ', number[int(len(number)/2)])
else:
    s = number[int(len(number)/2)] + number[int(len(number)/2 - 1)]
    print('The median is: ', s/2)



# N50 
half = total/2
count = 0
for num in number:
    count += num
    if count >= half:
        print("The N50 is: ", num)
        break