#Problem 2
#
#Write a function that combines two lists by 
#alternatingly taking elements. For example: 
#given the two lists [a, b, c] and [1, 2, 3], 
#the function should return [a, 1, b, 2, c, 3].

def alternate(arr1, arr2):
    
    newArray = []
    
    while ((len(arr1) + len(arr2)) > 0):
        newArray.append(arr1[0])
        arr1.pop(0)
        newArray.append(arr2[0])
        arr2.pop(0)
        
    return newArray



testArrayOne = ['a', 'b', 'c', 'd', 'e']
testArrayTwo = [1, 2, 3, 4, 5]

print alternate(testArrayOne, testArrayTwo)
print alternate(testArrayOne, testArrayTwo)
