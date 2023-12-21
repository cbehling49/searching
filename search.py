"""
Project 1 - Searching
Cody Behling
CS-2420-601
"""

# library imports needed for program to run properly
import random
import time
from math import sqrt


def linear_search(lyst, target):
    """
    Search `lyst` via linear search.

    Iterates through `lyst` index by index.
    Starts at the first index (lyst[0]).
    Checks each element until `target` is found or the end of `lyst` is reached.

    Cases
    -----
    Best case : 1
    Worst case : n

    Parameters
    ----------
    lyst : list
        Random list from `main()`.
    target : int
        This iteration's current target.

    Returns
    -------
    bool
        `True` if `target` is found in `lyst`.
        `False` if `target` is not found in `lyst`.
    """

    # assign variable
    i = 0

    # loop to iterate through `lyst`
    while i <= len(lyst) - 1:
        # check if the current index is `target` before moving to the next
        if lyst[i] == target:
            return True
        # if current index isn't `target`, move to the next
        else:
            i += 1
    return False


def binary_search(lyst, target):
    """
    Search `lyst` via binary search.

    Checks if the current element is less than, greater than, or equal to `target`.
    Starts at the middle index ((0 + len(lyst) - 1) // 2).
    Checks each element until `target` is found or the `lyst` range cannot be reduced further.

    Cases
    -----
    Best case : 1
    Worst case : (log2n) + 1

    Parameters
    ----------
    lyst : list
        Random list from `main()`.
    target : int
        This iteration's current target.

    Returns
    -------
    bool
        `True` if `target` is found in `lyst`.
        `False` if `target` is not found in `lyst`.
    """

    # assign variables
    left = 0
    right = len(lyst) - 1
    middle = (left + right) // 2

    # loop to iterate through `lyst`
    while left <= right:
        # check if the current index is `target` before cutting remaining `lyst` in half
        if lyst[middle] == target:
            return True
        # reassign variables to cut out left half of remaining `lyst`
        elif lyst[middle] < target:
            left = middle
            middle = (left + right) // 2
            # in case the left and middle values happen to be the same
            if left == middle:
                middle += 1
            if middle >= len(lyst):
                break
        # reassign variables to cut out right half of remaining `lyst`
        else:
            right = middle
            middle = (left + right) // 2
            # in case the right and middle values happen to be the same
            if right == middle:
                middle = ((left + right) // 2) - 1
            if middle <= -1:
                break
    return False


def jump_search(lyst, target):
    """
    Search `lyst` via jump search.
    The final range left to check is searched via linear search.

    Checks if the current element is less than, greater than, or equal to `target`.
    Starts at the first index (lyst[0]) and jumps a certain amount of indexes before checking again.
    Checks each element until `target` is found or the `lyst` range cannot be reduced further.

    Cases
    -----
    Best case : 1 + 1
    Worst case : n/sqrt(n) + sqrt(n) - 1 = 2sqrt(n) - 1

    Parameters
    ----------
    lyst : list
        Random list from `main()`.
    target : int
        This iteration's current target.

    Returns
    -------
    bool
        `True` if `target` is found in `lyst`.
        `False` if `target` is not found in `lyst`.
    """

    # assign variables
    step = sqrt(len(lyst))
    pre_index = 0
    next_index = int(pre_index + step)

    # loop to iterate through `lyst`
    while next_index <= len(lyst):
        # check if the current index is `target` before jumping
        if lyst[pre_index] == target:
            return True
        # reassign variables to make the jump
        elif lyst[next_index - 1] < target:
            pre_index = next_index
            next_index = int(pre_index + step)
            # change `next_index` before the while loop iterates and breaks
            if next_index > len(lyst):
                next_index = len(lyst) - 1
        # perform a linear search on the final portion of `lyst`
        else:
            new_lyst = lyst[pre_index: min(next_index, len(lyst))]
            remainder = linear_search(new_lyst, target)
            # if `target` is in `new_lyst`
            return remainder
        # break loop if the length of `lyst` is reached
        if pre_index >= len(lyst):
            break
    return False


def main():
    """
    Non-interactive main function.
    Calls and times iterating functions and targets.
    Prints results.
    """

    # assign variables
    random.seed(1)
    my_list = random.sample(range(100000000), k=100000000)
    my_list.sort()
    left = 0
    right = len(my_list) - 1
    middle = (left + right) // 2
    my_target = [int(my_list[0]), int(my_list[middle]), int(my_list[-1]), -1]
    my_functions = [linear_search, binary_search, jump_search]

    # set `target` for next iteration of search functions
    for i in my_target:
        # set search function for this iteration's `target`
        for j in my_functions:
            # start timer
            start_time = time.perf_counter()
            # call current function
            result = j(my_list, i)
            # stop timer
            end_time = time.perf_counter()
            # calculate duration of search
            elapsed_time = end_time - start_time
            # assign current function to variable to be printed later

            # print the times it took to search for the target using each method
            if result:
                print(f"{i} was found in {elapsed_time:0.7f} seconds.")
            else:
                print(f"{i} was not found, but searched for {elapsed_time:0.7f} seconds.")


if __name__ == "__main__":
    main()
