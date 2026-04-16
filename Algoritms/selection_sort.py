from typing import MutableSequence

def selectio_sort(array):
    
    for i in range(len(array) -1):
        lowest_numeber_index = i
        for j in range(i + 1, len(array)):
            if array[j] < array[lowest_numeber_index]:
                lowest_numeber_index = j
                
        if lowest_numeber_index != i:
            array[j],  array[lowest_numeber_index] = array[lowest_numeber_index], array[i]
    
    return array

def bubble_sort(data: MutableSequence) -> None:
    """Sort a mutable sequence(eg. List or array) in place"""
    
    for sorted_patition in range(len(data) -1, 0, -1):
        for i in range(sorted_patition):
            if data[i] > data[i + 1]:
               data[i], data[i + 1] = data[i + 1], data[i]
    
    print(f"End of pass {sorted_patition}, 'data' is now {data}")

if __name__ == "__main__":
    numbers = [2, 4, 1, 3, 5]
    print(f"Before sorting: {numbers}")
    
    print(f"Sorting {numbers}")
    bubble_sort(numbers)
    print(f"After sorting: {numbers}")
    