def binary_search(a: list[int], key: int) -> int:
    """Thực hiện tìm kiếm nhị phân trên danh sách đã sắp xếp.

    Điểm khác biệt so với C++: Không cần thủ công ép kiểu size_t hay quản lý
    chỉ số phức tạp, ta có thể dùng trực tiếp hàm len() và phép chia nguyên // của Python.
    """
    lo = 0
    hi = len(a) - 1
    
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if a[mid] == key:
            return mid
        elif a[mid] < key:
            lo = mid + 1
        else:
            hi = mid - 1
            
    return -1