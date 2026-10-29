"""Implement the insertion-sort exercise translated from C++."""


def insertion_sort(nums: list[int]) -> list[int]:
    """Sort integers in place with insertion sort and return the same list."""
    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > key:
            nums[j + 1] = nums[j]
            j -= 1

        nums[j + 1] = key

    return nums


if __name__ == "__main__":
    numbers = [5, 2, 4, 1, 3]
    result = insertion_sort(numbers)
    print(result)
