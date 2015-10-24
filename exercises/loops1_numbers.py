n = 1000
numbers = range(2,n)
print numbers
result = []
while len(numbers)>0:
    result.append(numbers[0])    
    dell = [i for i in numbers if i % numbers[0] == 0]    
    for i in dell:
        numbers.remove(i)

print result
print len(result)