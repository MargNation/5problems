// Problem 4

// Write a function that given a list of non negative integers, 
// arranges them such that they form the largest possible number. 

// For example, given [50, 2, 1, 9], the largest formed number is 95021.

function findLargestNum(arr) {
  var firstNum = arr[0].toString();
  for (var i = 1; i < arr.length; i++) {
    if (firstNum + arr[i] > arr[i] + firstNum) {
      firstNum += arr[i];
      } else {
        firstNum = (arr[i] + firstNum);
      }
  }
  return firstNum;
}

var testArray1 = [50, 2, 1, 9];
console.log('testArray1: ', findLargestNum(testArray1));
var testArray2 = [9, 90];
console.log('testArray2: ', findLargestNum(testArray2));
var testArray3 = [8, 8, 8];
console.log('testArray3: ', findLargestNum(testArray3));
var testArray4 = [1, 2, 3, 4, 5, 6, 7, 8, 9];
console.log('testArray4: ', findLargestNum(testArray4));
