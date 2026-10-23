#translate.py
def insertion_sort(nums : list[int]) -> list[int]:
    """Sort a list of integers in ascending order using insertion sort."""
    for i in range(1 , len(nums)):
        key = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > key:
            nums[j + 1] = nums[j]
            j -= 1

        nums[j + 1] = key

    return nums


numbers = [5, 2, 4, 1, 3]
result = insertion_sort(numbers)

print(result)