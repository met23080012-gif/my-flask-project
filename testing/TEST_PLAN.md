# TEST PLAN – Student Score Calculator

## 1. Mục tiêu

Kiểm thử chức năng `/score` của ứng dụng Flask Student Score Calculator.

Mục tiêu kiểm thử:

- Kiểm tra dữ liệu điểm hợp lệ.
- Kiểm tra dữ liệu không hợp lệ.
- Kiểm tra dữ liệu rỗng hoặc thiếu.
- Kiểm tra các giá trị tại Boundary.
- Kiểm tra Error Handling.
- Kiểm tra HTTP Status Code.
- Kiểm tra kết quả xếp loại.

---

## 2. Specification

Quy tắc xếp loại:

| Khoảng điểm | Xếp loại |
|---|---|
| 0 <= score < 5 | Yếu |
| 5 <= score < 6.5 | Trung bình |
| 6.5 <= score < 8 | Khá |
| 8 <= score <= 10 | Giỏi |

Validation:

- Score phải được cung cấp.
- Score không được rỗng.
- Score phải là số.
- Score phải nằm trong khoảng 0 đến 10.
- Dữ liệu không hợp lệ trả về HTTP 400.
- Dữ liệu hợp lệ trả về HTTP 200.

---

## 3. Test Cases

| ID | Scenario | Input | Type | Expected Result |
|---|---|---|---|---|
| TC01 | Điểm hợp lệ – Giỏi | 8.5 | Normal | HTTP 200, Giỏi |
| TC02 | Điểm hợp lệ – Khá | 7.0 | Normal | HTTP 200, Khá |
| TC03 | Điểm hợp lệ – Trung bình | 5.5 | Normal | HTTP 200, Trung bình |
| TC04 | Điểm hợp lệ – Yếu | 3.0 | Normal | HTTP 200, Yếu |
| TC05 | Biên dưới tuyệt đối | 0 | Boundary | HTTP 200, Yếu |
| TC06 | Biên trên tuyệt đối | 10 | Boundary | HTTP 200, Giỏi |
| TC07 | Ngay dưới mốc 5 | 4.9 | Boundary | HTTP 200, Yếu |
| TC08 | Đúng mốc 5 | 5.0 | Boundary | HTTP 200, Trung bình |
| TC09 | Ngay dưới mốc 6.5 | 6.4 | Boundary | HTTP 200, Trung bình |
| TC10 | Đúng mốc 6.5 | 6.5 | Boundary | HTTP 200, Khá |
| TC11 | Ngay dưới mốc 8 | 7.9 | Boundary | HTTP 200, Khá |
| TC12 | Đúng mốc 8 | 8.0 | Boundary | HTTP 200, Giỏi |
| TC13 | Điểm nhỏ hơn 0 | -1 | Invalid | HTTP 400 |
| TC14 | Điểm lớn hơn 10 | 11 | Invalid | HTTP 400 |
| TC15 | Dữ liệu không phải số | abc | Invalid | HTTP 400 |
| TC16 | Score rỗng | /score?score= | Empty | HTTP 400 |
| TC17 | Thiếu tham số score | /score | Empty | HTTP 400 |
| TC18 | Giá trị NaN | nan | Error Handling | HTTP 400 |

---

## 4. Test Environment

- Operating System: Windows
- Programming Language: Python
- Web Framework: Flask
- Testing Framework: pytest
- IDE: Visual Studio Code
- Browser: Google Chrome

---

## 5. Test Strategy

Testing sẽ được thực hiện theo các nhóm:

1. Normal Case
2. Boundary Value Analysis
3. Invalid Data
4. Empty Data
5. Error Handling

Automated Testing sẽ được thực hiện bằng pytest.

---

## 6. Expected Testing Flow

```text
Test Case
    ↓
Automated Test
    ↓
Run Test
    ↓
PASS / FAIL
    ↓
Nếu FAIL
    ↓
Phân tích Root Cause
    ↓
Fix Code
    ↓
Re-test
    ↓
PASS