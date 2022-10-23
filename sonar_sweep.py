## Juice Analytics 
## Assessment - Dwight Lindquist 

## Problem: Advent of Code - Sonar Sweep

## given an array of numbers, count the number of times the value increases from one to the next 
## [3, 5, 1, 2] >> returns "2", because it increased from 3 to 5 and from 1 to 2 

def count_depth_increases(arr): 
  items = list(arr) 
  p1 = 0 
  p2 = 1 
  count = 0 
  while p2 <= len(items) - 1: 
    if items[p1] < items[p2]: 
      count += 1 
    p1 += 1 
    p2 += 1 
  return count 

print(count_depth_increases([1,5,2,4]))
print(count_depth_increases([1,5,5,4]))