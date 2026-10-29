def is_palindrome(s: str) -> bool:
    """
    Kiểm tra chuỗi đối xứng bằng cách dùng 2 con trỏ (giống C++).
    
    Khác biệt so với C++:
    1. Không cần khai báo kiểu dữ liệu cho biến (như int left = 0).
    2. Không cần thư viện phụ trợ, cú pháp gọn gàng hơn.
    """
    left = 0
    right = len(s) - 1
    
    while left < right:
        if s[left] != s[right]:
            return False  
        left += 1
        right -= 1
        
    return True