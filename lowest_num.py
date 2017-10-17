#!/usr/bin/env python
############################################
#  Function to return a new list, with the #
#  smallest number from an existing list.  #
############################################

def smallest_num(numbers):
    
    smallest = min(numbers)
    list_with_smallest = [smallest]
    numbers.remove(smallest)
    
    return list_with_smallest

print (smallest_num([1, 13, -5, 99]))

