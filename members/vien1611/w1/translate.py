import time
import sys

def fibonacci_recursive(n):
    """
    Tính số Fibonacci thứ n bằng phương pháp đệ quy.
    Độ phức tạp thời gian: O(2^n) - Rất chậm với n lớn.
    """
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

def fibonacci_iterative(n):
    """
    Tính số Fibonacci thứ n bằng phương pháp khử đệ quy (vòng lặp).
    Độ phức tạp thời gian: O(n) - Nhanh và tối ưu bộ nhớ O(1).
    """
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

# Bắt buộc gom phần chạy trực tiếp vào khối này để pytest không bị lỗi khi import
if __name__ == "__main__":
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 35

    print(f"--- So sánh tính Fibonacci({n}) ---")

    start_time = time.perf_counter()
    res_iterative = fibonacci_iterative(n)
    end_time = time.perf_counter()
    print(f"[Khử đệ quy] Kết quả: {res_iterative} | Thời gian: {end_time - start_time:.6f} giây")

    start_time = time.perf_counter()
    res_recursive = fibonacci_recursive(n)
    end_time = time.perf_counter()
    print(f"[Đệ quy]     Kết quả: {res_recursive} | Thời gian: {end_time - start_time:.6f} giây")