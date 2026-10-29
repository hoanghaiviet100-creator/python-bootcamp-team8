# translate.py

def bubble_sort(arr: list[int]) -> list[int]:
    """
    Sắp xếp danh sách số nguyên theo thứ tự tăng dần bằng thuật toán Bubble Sort.
    Key difference from C++:
    In C++, swapping two elements requires a temporary variable (e.g., `int temp = a[i];`) 
    or calling `std::swap()`, and passing arrays often involves pointers or reference types (`vector<int>&`). 
    In Python, we perform tuple unpacking (`a[j], a[j+1] = a[j+1], a[j]`) to swap elements directly in a single line,
    making the code cleaner and more Pythonic.
    """
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

    return arr


