def function(a, b):
    return str(a) + str(b)

result = function(5, '10')
print(result)

#Alternative solution
def function(a, b):
    return int(a) + int(b) #This solution will only work if both inputs are convertible to integers.
result = function(5, 10)
print(result)