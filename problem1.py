#Problem 1
#
#Write three functions that compute the sum of the 
#numbers in a given list using a for-loop, 
#a while-loop, and recursion.

def forLoop(arr):
    runningSum = 0
    for i in range(len(arr)):
        runningSum += arr[i]
    return runningSum

def whileLoop(arr):
    runningSum = 0
    counter = 0
    while (counter != len(arr)):
        runningSum += arr[counter]
        counter += 1
    return runningSum

def recursive(arr):
    runningSum = 0
    if len(arr) == 1:
        return arr[0]
    else:
        return arr[0] + recursive(arr[1:])
    

testArray = [1, 2, 3, 4, 5] #sum is 15
print forLoop(testArray)
print whileLoop(testArray)
print recursive(testArray)
