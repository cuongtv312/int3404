# Homework 2

## Phần cơ bản
- Làm quen với các hàm cơ bản của opencv2 và numpy: đọc, ghi, biểu diễn
- Làm quen với không gian màu cơ bản

Dữ liệu các bạn tải về trên website môn học.
Mỗi task được lập trình bởi 1 hàm trong file `week02.py` 

+ `q_0`: Đọc vào file ảnh, biểu diễn và ghi lại thành 1 file ảnh mới bằng opencv.
Tìm hiểu ý nghĩa của tham số trong hàm cv2.waitKey(a)

+ `q_1`: Đọc vào file `chromatic aberration.png`. In ra kích thước của ảnh.
Tìm hiểu thứ tự các kênh màu khi đọc bằng lệnh cv2.imread().
Sử dụng hàm của opencv2 để chuyển về kênh màu YCbCr, in ra giá trị trung bình của mỗi
kênh màu trên toàn ảnh. Làm tương tự với kênh màu RGB.    

+ `q_2`: Đọc vào file `apple.png`. Cắt quả táo ở đầu hàng (rõ nhất) và cuối hàng (mờ nhất),
lần lượt lưu lại dưới tên `clear_apple.png` và `blurred_apple.png`


## Phần nâng cao 

+ `q_3`: Sử dụng file `font.png`. Đọc vào kênh màu xám. Lần lượt lấy mẫu giảm kích thước (downsampling)
với giá trị xuống k/2, k/4, k/6, k/8, k/16, ... với k là kích thước của ảnh.
So sánh độ chi tiết của ảnh này với ảnh ban đầu (các phần bị ảnh hưởng do phép lấy mẫu sampling). 
Tính độ đo `Peak Signal to Noise (PSNR)` bằng cách dùng hàm cv2.resize để đổi về kích thước ban đầu.    

+ Tìm hiểu cách giảm hiệu ứng sắc sai, áp dụng với file `chromatic_aberration.png`

+ Hình ảnh quả táo bị mờ trong file `apple.png` là do hiệu ứng nào.
Tìm hiểu các phương pháp có thể áp dụng làm sắc nét ảnh.
