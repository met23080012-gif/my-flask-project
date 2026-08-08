# TEST REPORT – Student Score Calculator

## 1. Tổng quan

Dự án được kiểm thử bằng Python Flask và pytest.

Mục tiêu:
- Kiểm tra chức năng tính điểm và xếp loại.
- Kiểm tra dữ liệu hợp lệ và không hợp lệ.
- Kiểm tra Boundary Case.
- Kiểm tra Error Handling.
- Phát hiện và sửa lỗi thông qua Automated Testing.

---

## 2. Môi trường kiểm thử

- OS: Windows
- Python: 3.14.6
- Framework: Flask
- Testing Framework: pytest 9.1.1
- IDE: Visual Studio Code
- Browser: Google Chrome

---

## 3. Tổng kết Test

| Chỉ tiêu | Kết quả |
|---|---:|
| Tổng số Test Case | 18 |
| PASS trước khi sửa | 17 |
| FAIL trước khi sửa | 1 |
| PASS sau khi sửa | 18 |
| FAIL sau khi sửa | 0 |

---

## 4. Test Fail được phát hiện

### Test Case

TC18 – Kiểm tra giá trị NaN.

### Input

```text
/score?score=nan